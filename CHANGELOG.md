# Changelog

## Unreleased

- Kept the skill's working contract concise by default; the full eleven-field template is for explicit handoffs and optional CLI workflows.

## 0.0.1 — 2026-11-02

- Added complete English and Russian guides. English is canonical; paired translations are updated together.
- Added bilingual contribution guidance and a private GitHub vulnerability reporting procedure.
- Removed personal project context from public documentation and clarified implementation limits and evidence boundaries.
- Pinned GitHub Actions to verified full commit SHAs and added job timeouts and least-privilege permissions.
- Preserved both the pre-existing GitHub history and the complete local project history.
- GitHub-hosted CI passed on Windows and Ubuntu with Python 3.10 and 3.13 (run [41435571456](https://github.com/Sashido01/ScopeAnchor/actions/runs/41435571456), commit `dbc291a1efc1b4c7259fbee00701bb9821d46536`).

## 0.0.0 — 2026-11-02

- Created the standalone native Codex skill `scope-anchor`, without a Claude plugin dependency.
- Added an offline CLI for task contracts and local decisions, structural tests, and Windows/Linux CI.
- Documented the stack, limits, provenance, security, acceptance checks, and Git workflow.
- Measured Codex quota savings: `NOT_VERIFIED`.
