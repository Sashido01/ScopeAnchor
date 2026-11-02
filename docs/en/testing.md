# Testing and verification

Run the commands in [development](development.md) from the repository root. The unit suite currently covers contract parsing, CLI subprocess behavior, duplicate and malformed JSON, Unicode decision round trips, explicit replacement, symlink rejection where supported, and refusal to overwrite task files.

The CI matrix is Windows and Ubuntu with Python 3.10 and 3.13. Only a completed GitHub Actions run proves the hosted result for a commit. Local checks prove only the current local environment. Neither set proves Codex automatic discovery or successful model execution.

Documentation checks should verify relative links, the skill manifest and referenced files, matching English/Russian examples and status statements, and absence of local data or secrets in the staged tree and reachable commit history.
