# Architecture

## Components

- `.agents/skills/scope-anchor/SKILL.md` is the native skill entry point; `references/` holds additional instructions opened when relevant.
- `src/scope_anchor.py` is an optional, offline CLI implemented with Python's standard library.
- `.scope-anchor/decisions.json` is an explicitly chosen local data file and is ignored by Git by default.
- `tests/` checks deterministic CLI behavior; GitHub Actions runs the checks on Windows and Ubuntu.

## Data flow

The user requests work in Codex. Codex reads applicable project instructions and the skill, inspects the repository, carries out the task, and reports evidence. Separately, the CLI can create or validate a Markdown contract and print it to stdout. It does not call Codex, execute contract content, access a model, or contact a service.

## Boundaries

Inputs are untrusted text. The CLI checks structure and selected file properties, but it cannot determine whether prose is true, safe, complete, or semantically consistent. It does not prevent a person from sharing sensitive content in a compiled contract. The skill is guidance, not a permission system or a security sandbox.

English is canonical. Each English guide has a Russian counterpart under `docs/ru/`; behavior, commands, limitations, and statuses must be updated together.
