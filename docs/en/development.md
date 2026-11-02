# Development

## Requirements

Python 3.10+; no third-party dependencies are needed. The project targets Windows and Ubuntu. The CI matrix uses Python 3.10 and 3.13 on both operating systems.

## Checks

```console
python -m unittest discover -s tests -v
python -m compileall -q src
python src/scope_anchor.py check examples/complete-task.md --json
python src/scope_anchor.py compile examples/complete-task.md
git diff --check
```

On Windows use `py -3` when needed; on Ubuntu use `python3`. The project tests include CLI subprocess coverage and local decision-file round trips. A local test is not evidence that GitHub-hosted CI passed.

## Change rules

Keep code offline and in the standard library. Update the English page and its Russian counterpart in the same change. Pin workflow actions to verified full commit SHAs, retain read-only `GITHUB_TOKEN` permissions, and use bounded jobs. Never include private user data in fixtures or logs.

See [contribution guidance](../../CONTRIBUTING.md) and [testing notes](../TESTING.md).
