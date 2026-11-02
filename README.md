[English](README.md) | [Русский](README.ru.md)

# ScopeAnchor

**A native Codex skill for structured engineering tasks, reproducible workflows, and quota-aware execution.** ScopeAnchor turns a complex request into a bounded execution contract while keeping Codex responsible for the actual work.

**Version:** 0.0.1 · **License:** MIT · **Runtime:** Python 3.10+ for the optional CLI; no runtime dependency for the skill.

## What it does

- Guides Codex to inspect repository instructions and current state before editing.
- Audits task requests for repeated or conflicting directions, missing acceptance criteria, unclear stack/runtime, irrelevant context, and unjustified scope.
- Makes goal, scope, non-goals, constraints, acceptance checks, stop condition, and report explicit.
- Preserves decisions as advisory context and keeps unknown facts marked as unknown.
- Recommends a minimally sufficient model and reasoning effort; it never changes the user's selected model or Codex settings.
- Provides an offline CLI to create, validate, compile, and manage local task contracts and decisions.
- Keeps private decisions in `.scope-anchor/`, which Git ignores by default.

The skill is the primary interface. The CLI is an optional helper and does not invoke Codex, a model, shell commands, or network services.

For ordinary multi-step engineering, its default recommendation is GPT-6 Luna Medium; Low is for simple editorial or mechanical work, and High requires a concrete complexity or error-cost reason. This guidance is advisory and does not identify or change the model selected in Codex.

## Quick start

Install the skill in a project by copying `.agents/skills/scope-anchor/` into that project's `.agents/skills/` directory. Inspect an existing destination before updating it; do not overwrite a customized skill blindly. In Codex, ask:

```text
Use $scope-anchor to implement this task: <task>
```

Codex discovers project skills from `.agents/skills/`. The skill can also be read and followed manually; installing it does not require changing global Codex settings.

## Optional CLI

Run from the repository root with Python 3.10 or newer:

```console
python src/scope_anchor.py --help
python src/scope_anchor.py new --out TASK.md --goal "Fix the export regression"
python src/scope_anchor.py check TASK.md --json
python src/scope_anchor.py compile TASK.md
```

`new` creates an intentionally incomplete template with `TODO` markers and refuses to overwrite a file. Fill in the required sections before `check` or `compile`. `compile` prints the validated contract to standard output; it does not save or submit it.

Record a local decision (do not store secrets):

```console
python src/scope_anchor.py lock --file .scope-anchor/decisions.json --key ui.window --value "Use one window"
python src/scope_anchor.py decisions --file .scope-anchor/decisions.json
python src/scope_anchor.py unlock --file .scope-anchor/decisions.json --key ui.window
```

Use `--replace` to intentionally change an existing decision key. Commands only read or modify the explicitly named paths. See [usage](docs/en/usage.md) for Windows and Ubuntu examples.

## Install and develop

No package installation or third-party Python dependency is required. On Windows, use PowerShell and `py -3` or `python`; on Ubuntu, use `python3`. The skill itself only needs Codex to read its files. See [installation](docs/en/installation.md) and [development](docs/en/development.md).

## Design and limits

ScopeAnchor consists of a native `SKILL.md`, small reference documents, an offline standard-library Python CLI, and tests. It does not provide an AI gateway, server, web interface, database, telemetry, or automatic publishing. The CLI validates structure and selected safety properties; it cannot establish that a task is correct, resolve semantic contradictions by itself, or guarantee successful execution. Model-routing guidance is advisory. Token savings and automatic skill activation have not been measured or guaranteed.

English is the canonical source language for project documentation. Paired Russian documents are maintained in the same change and reviewed for equivalent requirements, examples, and status claims. See [architecture](docs/en/architecture.md), [security](SECURITY.md), and [provenance](docs/PROVENANCE.md).

## Contributing and security

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Report vulnerabilities through the repository's private vulnerability reporting form at [GitHub Security Advisories](https://github.com/Sashido01/ScopeAnchor/security/advisories/new); do not post exploit details in public issues. See [SECURITY.md](SECURITY.md) for the reporting procedure.

## License

MIT. See [LICENSE](LICENSE).
