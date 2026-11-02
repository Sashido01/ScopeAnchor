# Getting started

ScopeAnchor is primarily a native Codex Agent Skill. Its optional Python CLI helps prepare and validate a structured task contract; it does not perform the task.

## Use the skill

1. Copy `.agents/skills/scope-anchor/` into the target repository's `.agents/skills/` directory. Review an existing destination before replacing or merging it.
2. Start a Codex conversation in that repository and explicitly request `$scope-anchor` for a multi-step engineering task.
3. Let the skill audit the request and inspect the repository's own `AGENTS.md`, source, and tests before proposing changes. It checks for repetition, conflicts, missing acceptance criteria, unstated tooling, irrelevant context, and scope expansion.
4. Review the scope, acceptance checks, and final evidence. Skill guidance does not override user instructions or host permissions.

Project skill discovery depends on the Codex host and context. Installing files does not change global configuration, and the CLI cannot verify discovery or activation.

## Use the CLI

Python 3.10+ is needed only for the CLI. From the repository root:

```console
python src/scope_anchor.py new --out TASK.md --goal "Document the import behavior"
```

Fill the template's `TODO` values, then run `check` and `compile`. See [installation](installation.md) and [usage](usage.md).
