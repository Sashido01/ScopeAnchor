#!/usr/bin/env python3
"""Offline, dependency-free task-contract helper for the ScopeAnchor Codex skill.

This script never invokes a model, Git, a subprocess, or the network.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

FIELDS = (
    "GOAL", "SCOPE", "NON-GOALS", "CURRENT STATE", "LOCKED SEMANTICS",
    "INVARIANTS", "FILES", "ACCEPTANCE", "TESTS", "STOP", "REPORT",
)
HEADING = re.compile(r"^## ([A-Z][A-Z -]*)\s*$")
KEY = re.compile(r"^[a-z][a-z0-9_.-]{0,79}$")
PLACEHOLDER = re.compile(r"\bTODO\s*:", re.IGNORECASE)
SCOPES = ("all", "project", "session")
MAX_FILE_BYTES = 512 * 1024


class ContractError(Exception):
    """A validated user-input error, suitable for concise CLI reporting."""


def read_text(path: Path) -> str:
    if path.is_symlink():
        raise ContractError(f"Symbolic links are not accepted: {path}")
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            raise ContractError(f"Input too large (limit {MAX_FILE_BYTES} bytes): {path}")
        return path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        raise ContractError(f"Cannot read {path}: {exc}") from exc


def reject_redirected_path(path: Path) -> None:
    """Reject symlinked or junction path components before writing user data."""
    for candidate in (path, *path.parents):
        if candidate.is_symlink():
            raise ContractError(f"Symbolic links are not accepted: {candidate}")
        is_junction = getattr(candidate, "is_junction", None)
        if callable(is_junction) and is_junction():
            raise ContractError(f"Junctions are not accepted: {candidate}")


def parse_contract(content: str) -> tuple[dict[str, str], list[str]]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    errors: list[str] = []
    for lineno, line in enumerate(content.splitlines(), start=1):
        match = HEADING.fullmatch(line.rstrip())
        if match:
            name = match.group(1)
            if name not in FIELDS:
                errors.append(f"line {lineno}: unexpected section {name}")
                current = None
            elif name in sections:
                errors.append(f"line {lineno}: duplicate section {name}")
                current = None
            else:
                sections[name] = []
                current = name
        elif current is not None:
            sections[current].append(line)
    data = {name: "\n".join(value).strip() for name, value in sections.items()}
    for name in FIELDS:
        if name not in data:
            errors.append(f"missing section {name}")
        elif not data[name]:
            errors.append(f"empty section {name}")
        elif PLACEHOLDER.search(data[name]):
            errors.append(f"placeholder in section {name}")
    return data, errors


def load_contract(path: Path) -> tuple[dict[str, str], list[str]]:
    return parse_contract(read_text(path))


def create_contract(path: Path, title: str, goal: str, project: str) -> None:
    if not path.parent.is_dir():
        raise ContractError(f"Parent directory does not exist: {path.parent}")
    reject_redirected_path(path)
    if not goal.strip() or not title.strip():
        raise ContractError("Goal and title must be nonempty")
    safe_title = " ".join(title.split())
    safe_goal = " ".join(goal.split())
    safe_project = " ".join(project.split())
    if len(safe_title) > 150 or len(safe_goal) > 500 or len(safe_project) > 120:
        raise ContractError("Title, goal, or project exceeds the documented size cap")
    text = f"# TASK: {safe_title}\n\n"
    for field in FIELDS:
        if field == "GOAL":
            value = safe_goal
        elif field == "CURRENT STATE" and safe_project:
            value = f"Project: {safe_project}. TODO: inspect actual baseline in repository"
        else:
            value = "TODO: inspect the project or provide the required evidence"
        text += f"## {field}\n{value}\n\n"
    try:
        # Exclusive open is atomic and cannot accidentally overwrite existing work.
        with path.open("x", encoding="utf-8", newline="\n") as file:
            file.write(text)
    except OSError as exc:
        raise ContractError(f"Cannot create {path}; existing files are never overwritten: {exc}") from exc


def read_decisions(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        raise ContractError(f"Decision file not found: {path}")
    def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ContractError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    try:
        document: Any = json.loads(read_text(path), object_pairs_hook=reject_duplicate_keys)
    except ValueError as exc:
        raise ContractError(f"Invalid JSON in {path}: {exc}") from exc
    if (not isinstance(document, dict) or type(document.get("schema_version")) is not int
            or document.get("schema_version") != 1):
        raise ContractError("Decision file requires schema_version=1")
    obj = document.get("decisions")
    if not isinstance(obj, dict) or len(obj) > 100:
        raise ContractError("decisions must be an object with at most 100 entries")
    for key, record in obj.items():
        if not isinstance(key, str) or not KEY.fullmatch(key):
            raise ContractError(f"Invalid decision key: {key!r}")
        if not isinstance(record, dict) or set(record) != {"value", "scope"}:
            raise ContractError(f"Invalid decision record: {key}")
        value, scope = record["value"], record["scope"]
        if (not isinstance(value, str) or not value.strip() or len(value) > 300
                or "\n" in value or "\r" in value):
            raise ContractError(f"Invalid decision value for: {key}")
        if scope not in SCOPES:
            raise ContractError(f"Invalid decision scope for: {key}")
    return obj


def atomic_save_decisions(path: Path, decisions: dict[str, dict[str, str]]) -> None:
    if path.is_symlink() or path.suffix.lower() != ".json":
        raise ContractError("Decisions must be saved to an explicit nonsymlink .json path")
    reject_redirected_path(path)
    if not path.parent.exists():
        # Only the explicitly requested decision-file parent is created.
        path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps({"schema_version": 1, "decisions": decisions},
                         ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if len(payload.encode("utf-8")) > MAX_FILE_BYTES:
        raise ContractError("Decision document exceeds size cap")
    temporary: str | None = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                                         dir=path.parent, prefix=".decisions-",
                                         suffix=".tmp", delete=False) as dest:
            temporary = dest.name
            dest.write(payload)
        os.replace(temporary, path)
    except OSError as exc:
        raise ContractError(f"Cannot write {path}: {exc}") from exc
    finally:
        if temporary is not None:
            try:
                Path(temporary).unlink(missing_ok=True)
            except OSError:
                pass


def print_validation(path: Path, json_output: bool) -> int:
    data, errors = load_contract(path)
    result = {"status": "PASS" if not errors else "FAIL",
              "sections": len(data), "expected_sections": len(FIELDS), "errors": errors}
    if json_output:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"{result['status']}: {len(data)}/{len(FIELDS)} sections")
        for error in errors:
            print(f" - {error}")
    return 0 if not errors else 2


def compile_contract(path: Path, decisions_path: Path | None) -> str:
    data, errors = load_contract(path)
    if errors:
        raise ContractError("Contract invalid: " + "; ".join(errors))
    decisions = read_decisions(decisions_path) if decisions_path else {}
    lines = ["# Bounded Codex execution request", "",
             "Follow applicable AGENTS.md and the user's latest explicit instructions.",
             "Inspect actual repository state; do not invent evidence or change model/config.",
             "Do the requested work; stop when ACCEPTANCE is met; report NOT_VERIFIED honestly.", ""]
    for field in FIELDS:
        lines.extend((f"## {field}", data[field], ""))
    if decisions:
        lines.append("## LOCAL ADVISORY DECISIONS")
        lines.append("Previous choices are defaults, not overrides of an explicit new user request.")
        for key, rec in sorted(decisions.items()):
            lines.append(f"- `{key}` ({rec['scope']}): {rec['value']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="scope_anchor.py", description="Offline task-contract CLI")
    sub = root.add_subparsers(dest="command", required=True)
    create = sub.add_parser("new", help="Create a non-overwriting task contract")
    create.add_argument("--out", required=True, type=Path)
    create.add_argument("--title", default="Bounded engineering task")
    create.add_argument("--goal", required=True)
    create.add_argument("--project", default="")
    check = sub.add_parser("check", help="Validate a task contract without modifying it")
    check.add_argument("path", type=Path)
    check.add_argument("--json", action="store_true")
    compile_cmd = sub.add_parser("compile", help="Print a complete contract as a Codex prompt")
    compile_cmd.add_argument("path", type=Path)
    compile_cmd.add_argument("--decisions", type=Path)
    lock = sub.add_parser("lock", help="Record one local, non-secret decision")
    lock.add_argument("--file", required=True, type=Path)
    lock.add_argument("--key", required=True)
    lock.add_argument("--value", required=True)
    lock.add_argument("--scope", choices=SCOPES, default="all")
    lock.add_argument("--replace", action="store_true", help="Replace an existing decision explicitly")
    unlock = sub.add_parser("unlock", help="Remove one specified local decision")
    unlock.add_argument("--file", required=True, type=Path)
    unlock.add_argument("--key", required=True)
    listing = sub.add_parser("decisions", help="Show keys and scopes without printing values")
    listing.add_argument("--file", required=True, type=Path)
    return root


def run(args: argparse.Namespace) -> int:
    command = args.command
    if command == "new":
        create_contract(args.out, args.title, args.goal, args.project)
        print(f"CREATED: {args.out} (fill TODO fields before compile)")
    elif command == "check":
        return print_validation(args.path, args.json)
    elif command == "compile":
        sys.stdout.write(compile_contract(args.path, args.decisions))
    elif command == "decisions":
        for key, rec in sorted(read_decisions(args.file).items()):
            print(f"{key}\t{rec['scope']}")
    elif command in ("lock", "unlock"):
        if not KEY.fullmatch(args.key):
            raise ContractError("Key must match [a-z][a-z0-9_.-]{0,79}")
        file: Path = args.file
        if file.is_symlink():
            raise ContractError("Symbolic links are not accepted")
        if command == "lock" and not file.exists():
            decisions: dict[str, dict[str, str]] = {}
        else:
            decisions = read_decisions(file)
        if command == "lock":
            if args.key in decisions and not args.replace:
                raise ContractError("Decision already exists; use --replace for explicit overwrite")
            value = args.value.strip()
            if not value or len(value) > 300 or "\n" in value or "\r" in value:
                raise ContractError("Value must be a nonempty single line up to 300 chars")
            if len(decisions) >= 100 and args.key not in decisions:
                raise ContractError("Decision limit (100) reached")
            decisions[args.key] = {"scope": args.scope, "value": value}
        else:
            if args.key not in decisions:
                raise ContractError("Decision key not found")
            del decisions[args.key]
        atomic_save_decisions(file, decisions)
        print(f"{'LOCKED' if command == 'lock' else 'UNLOCKED'}: {args.key}")
    return 0


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8")
    args = parser().parse_args(argv)
    try:
        return run(args)
    except ContractError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
