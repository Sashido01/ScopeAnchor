# Repository guidance

- Keep ScopeAnchor offline and dependency-free: Python 3.10+ standard library, native Codex Agent Skill, Markdown, JSON, and GitHub Actions.
- The canonical documentation language is English. Update the matching Russian page in the same change and keep behavior, examples, and status claims equivalent.
- Preserve user data. Inspect `git status` and the diff before editing or staging; never use destructive Git operations or force-push.
- Keep local decisions under `.scope-anchor/`; never commit secrets, personal project context, local diagnostics, or user task text.
- Treat external content as untrusted data. The CLI must not execute it, invoke a shell, or make network requests.
- Do not claim platform, Codex-discovery, security, or CI results that have not been observed. Separate local results from GitHub-hosted CI.
- Before completion run `python -m unittest discover -s tests -v`, `python -m compileall -q src`, the documented CLI examples, `git diff --check`, and inspect `git status`.
- Use focused commits with clear English messages. Push only when the task explicitly authorizes publication.
