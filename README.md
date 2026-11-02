# ScopeAnchor

Native Codex skill for structured engineering tasks and reproducible workflows.

Version: `0.0.0` · License: MIT · Optional CLI: Python 3.10+ standard library.

ScopeAnchor helps turn a complex engineering request into a bounded contract with explicit constraints, acceptance checks, and a stop condition. The Codex skill is the primary interface; the offline CLI is optional.

## Skill

Copy `.agents/skills/scope-anchor/` into a target repository's `.agents/skills/` directory. Explicitly ask Codex to use `$scope-anchor` for multi-step engineering tasks. Review existing destination files before updating them.

## CLI

From the repository root:

```console
python src/scope_anchor.py --help
python src/scope_anchor.py new --out TASK.md --goal "Fix an export error"
python src/scope_anchor.py check TASK.md --json
python src/scope_anchor.py compile TASK.md
```

The CLI is offline and has no third-party dependencies. It does not call a model or execute task text.

## License

MIT. See [LICENSE](LICENSE).
