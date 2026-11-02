# Troubleshooting

## `python` is not found or is too old

Check the interpreter version. On Windows try `py -3 --version`; on Ubuntu try `python3 --version`. The CLI requires Python 3.10 or newer.

## `new` cannot create a file

The parent directory must already exist. `new` deliberately refuses to overwrite an existing path. Choose a new output name; inspect an existing file before deciding how to update it.

## `check` reports missing sections or TODO values

Open the contract and fill every required section with concrete information or a clearly stated unknown. Do not mark unknown facts as verified. `compile` intentionally fails until validation succeeds.

## Skill is not activated

Confirm the directory is named `.agents/skills/scope-anchor/` and contains `SKILL.md` plus its references. Explicitly request `$scope-anchor`. Discovery and automatic activation depend on the Codex host and are not tested by the CLI.

## Security and data

The CLI does not redact contract text. Review it before sharing or compiling. Keep secrets and private task content out of contracts, decision files, examples, Issues, and logs. Report vulnerabilities through the private GitHub form described in [SECURITY.md](../../SECURITY.md).
