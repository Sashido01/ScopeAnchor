# Installation

ScopeAnchor has no package-install step and no third-party runtime dependencies. Choose the native skill, the optional CLI, or both.

## Project-local skill

Copy the complete `.agents/skills/scope-anchor/` directory into `.agents/skills/` of the target repository. Preserve its `SKILL.md`, `agents/openai.yaml`, and `references/` files. If a destination already exists, compare it and merge intentionally; do not overwrite customized files blindly.

## User-level skill

User-level skill locations and discovery behavior vary by Codex host. Prefer project-local installation when you need reproducible, repository-scoped instructions. Do not change global Codex configuration just to use ScopeAnchor.

## Python CLI

Install Python 3.10 or newer from your operating system's normal package source if needed. No `pip install` is required.

### Windows PowerShell

```powershell
py -3 --version
py -3 src/scope_anchor.py --help
```

### Ubuntu

```bash
python3 --version
python3 src/scope_anchor.py --help
```

Paths containing spaces are supported when passed as a single quoted argument, for example `--out "work files/TASK.md"`.
