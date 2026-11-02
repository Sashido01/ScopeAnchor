"""Deterministic offline regression tests for ScopeAnchor CLI."""

from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
import scope_anchor as sa  # noqa: E402


class ContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.folder = Path(self.tmp.name)
        self.example = ROOT / "examples" / "complete-task.md"

    def test_real_example_passes(self) -> None:
        fields, errors = sa.load_contract(self.example)
        self.assertFalse(errors)
        self.assertEqual(len(fields), 11)

    def test_new_is_intentionally_incomplete(self) -> None:
        p = self.folder / "TASK.md"
        sa.create_contract(p, "Test", "Fix export regression", "ExampleProject")
        data, errors = sa.load_contract(p)
        self.assertEqual(data["GOAL"], "Fix export regression")
        self.assertEqual(len(errors), 10)
        self.assertIn("Project: ExampleProject.", data["CURRENT STATE"])

    def test_existing_file_is_never_overwritten(self) -> None:
        p = self.folder / "task.md"
        p.write_text("user work", encoding="utf-8")
        with self.assertRaises(sa.ContractError):
            sa.create_contract(p, "Test", "Goal", "")
        self.assertEqual(p.read_text(encoding="utf-8"), "user work")

    def test_nonexistent_parent_rejected(self) -> None:
        with self.assertRaises(sa.ContractError):
            sa.create_contract(self.folder / "nested" / "TASK.md", "X", "Fix", "")
        self.assertFalse((self.folder / "nested").exists())

    def test_duplicate_and_unknown_section_rejected(self) -> None:
        original = self.example.read_text(encoding="utf-8")
        data, errors = sa.parse_contract(original + "\n## GOAL\nMore\n\n## SURPRISE\nX\n")
        self.assertIn("GOAL", data)
        self.assertTrue(any("duplicate" in e for e in errors))
        self.assertTrue(any("unexpected" in e for e in errors))

    def test_empty_section_rejected(self) -> None:
        content = self.example.read_text(encoding="utf-8")
        content = content.replace("## STOP\nПосле успешной приёмки остановить расширение задач и выдать полный отчёт.", "## STOP\n")
        _, errors = sa.parse_contract(content)
        self.assertTrue(any("empty section STOP" in e for e in errors))

    def test_missing_section_rejected(self) -> None:
        content = self.example.read_text(encoding="utf-8")
        content = content.replace("## GOAL\n", "### GOAL\n")
        _, errors = sa.parse_contract(content)
        self.assertTrue(any("missing section GOAL" in e for e in errors))

    def test_compile_preserves_fields(self) -> None:
        s = sa.compile_contract(self.example, None)
        self.assertIn("## ACCEPTANCE", s)
        self.assertIn("## INVARIANTS", s)
        self.assertIn("NOT_VERIFIED", s)
        self.assertNotIn("## LOCAL ADVISORY DECISIONS", s)

    def test_incomplete_compile_rejected(self) -> None:
        p = self.folder / "task.md"
        sa.create_contract(p, "Test", "Fix", "")
        with self.assertRaises(sa.ContractError):
            sa.compile_contract(p, None)

    def test_decision_lifecycle(self) -> None:
        p = self.folder / ".scope-anchor" / "decisions.json"
        self.assertEqual(sa.main(["lock", "--file", str(p), "--key", "ui.window",
                                  "--value", "Одно окно"]), 0)
        self.assertEqual(sa.read_decisions(p)["ui.window"]["value"], "Одно окно")
        with self.assertRaises(sa.ContractError):
            sa.run(sa.parser().parse_args(["lock", "--file", str(p),
                                           "--key", "ui.window", "--value", "Different"]))
        self.assertEqual(sa.main(["lock", "--file", str(p), "--key", "ui.window",
                                  "--value", "Новое", "--replace"]), 0)
        self.assertEqual(sa.read_decisions(p)["ui.window"]["value"], "Новое")
        self.assertEqual(sa.main(["unlock", "--file", str(p), "--key", "ui.window"]), 0)
        self.assertFalse(sa.read_decisions(p))

    def test_bad_decision_json_rejected(self) -> None:
        p = self.folder / "bad.json"
        p.write_text('{"schema_version":1,"decisions":{"bad":{"scope":"all"}}}', encoding="utf-8")
        with self.assertRaises(sa.ContractError):
            sa.read_decisions(p)

    def test_duplicate_json_decisions_rejected(self) -> None:
        p = self.folder / "dup.json"
        p.write_text('{"schema_version":1,"decisions":{},"decisions":{}}', encoding="utf-8")
        with self.assertRaises(sa.ContractError):
            sa.read_decisions(p)

    def test_symlink_decision_parent_rejected_if_supported(self) -> None:
        folder = self.folder / "real"
        folder.mkdir()
        link = self.folder / "alias"
        try:
            link.symlink_to(folder, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks not available")
        with self.assertRaises(sa.ContractError):
            sa.atomic_save_decisions(link / "decisions.json", {})

    def test_compile_with_decisions(self) -> None:
        s = sa.compile_contract(self.example, ROOT / "examples" / "decisions.example.json")
        self.assertIn("LOCAL ADVISORY DECISIONS", s)
        self.assertIn("runtime.native_first", s)

    def test_no_decision_values_in_listing(self) -> None:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertEqual(sa.main(["decisions", "--file", str(ROOT / "examples" / "decisions.example.json")]), 0)
        self.assertIn("runtime.native_first", buf.getvalue())
        self.assertNotIn("штатные механизмы", buf.getvalue())

    def test_symlink_reads_rejected_if_supported(self) -> None:
        p = self.folder / "link.md"
        try:
            p.symlink_to(self.example)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks not available")
        with self.assertRaises(sa.ContractError):
            sa.load_contract(p)

    def test_secret_unrelated_paths_are_not_written(self) -> None:
        outside = self.folder / "outside.txt"
        outside.write_text("unchanged", encoding="utf-8")
        task = self.folder / "TASK.md"
        sa.create_contract(task, "No writes", "Check", "")
        self.assertEqual(outside.read_text(encoding="utf-8"), "unchanged")
        self.assertEqual({p.name for p in self.folder.iterdir()}, {"outside.txt", "TASK.md"})

    def test_json_status_output(self) -> None:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = sa.print_validation(self.example, True)
        self.assertEqual(code, 0)
        obj = json.loads(buffer.getvalue())
        self.assertEqual(obj["status"], "PASS")
        self.assertEqual(obj["expected_sections"], 11)

    def test_command_line_subprocess(self) -> None:
        result = subprocess.run([sys.executable, str(ROOT / "src" / "scope_anchor.py"),
                                 "check", str(self.example), "--json"],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"PASS"', result.stdout)

    def test_skill_manifest_and_references(self) -> None:
        skill_path = ROOT / ".agents" / "skills" / "scope-anchor" / "SKILL.md"
        skill = skill_path.read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\nname: scope-anchor\ndescription: "))
        self.assertEqual(skill.count("\n---\n"), 1)
        for ref in ("task-contract", "routing", "verification"):
            self.assertTrue((skill_path.parent / "references" / f"{ref}.md").exists())
        self.assertNotIn("/plugin install", skill)

    def test_public_tree_keeps_local_decisions_ignored(self) -> None:
        ignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn(".scope-anchor/", ignore)
        self.assertIn(".env", ignore)


if __name__ == "__main__":
    unittest.main()
