# Usage

Run commands from the repository root. The CLI reads and writes UTF-8 text, and uses UTF-8 for stdout/stderr on supported text streams. It accesses only the paths supplied by the user. It has no network, shell execution, model, or telemetry feature.

## Create, validate, and compile a contract

```console
python src/scope_anchor.py new --out TASK.md --title "Fix export" --goal "Preserve Unicode in exported data"
python src/scope_anchor.py check TASK.md --json
python src/scope_anchor.py compile TASK.md
```

`new` creates an incomplete template and refuses to overwrite an existing file. `check` requires all eleven named sections and rejects missing, empty, duplicate, unexpected, or `TODO` content. `compile` fails for invalid input and prints a bounded prompt to stdout; redirecting the output is an explicit shell action by the caller.

## Save local decisions

```console
python src/scope_anchor.py lock --file .scope-anchor/decisions.json --key editor.format --value "Use the repository formatter"
python src/scope_anchor.py decisions --file .scope-anchor/decisions.json
python src/scope_anchor.py compile TASK.md --decisions .scope-anchor/decisions.json
python src/scope_anchor.py unlock --file .scope-anchor/decisions.json --key editor.format
```

Use `--replace` to intentionally change a key. `decisions` prints keys and scopes, not values. Do not store secrets, credentials, private task content, or personal data in decision files. `.scope-anchor/` is ignored by Git by default.

## Windows and Ubuntu paths

PowerShell example with a path containing spaces:

```powershell
py -3 src/scope_anchor.py new --out "work files/TASK.md" --goal "Check UTF-8 output"
```

Ubuntu example:

```bash
python3 src/scope_anchor.py new --out 'work files/TASK.md' --goal 'Check UTF-8 output'
```

The parent directory must already exist for `new`. Use quotes so the shell passes a path as one argument.
