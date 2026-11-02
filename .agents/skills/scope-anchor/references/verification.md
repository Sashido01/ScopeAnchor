# Native-first DevSecMLOps verification

1. Diagnose before edits: exact error, versions, command, affected path, observed environment; do not "fix" an unverified assumption.
2. Preserve OS-native update/install path, existing user config, runtime and permissions; no sidecar daemon or hooks to bypass product behavior.
3. Change minimal code/config; do not silently migrate storage or change finance/OCR semantics.
4. Before merging reuse: identify upstream origin and license, prove compatibility, record attribution. Never paste GPL/AGPL or no-license code into permissive core without explicit review.
5. Keep secrets out of logs/repo/PR: no tokens, private URLs, local chat history, credentials, real .env files or personal exports. Redact examples.
6. Run targeted checks; then prescribed release gates for platform(s) actually available. `NOT_VERIFIED` for Windows/macOS/physical hardware when not tested; don't extrapolate from Linux CI.
7. Document exact tested environment and reproducible commands, outcome and limitations; keep local Git clean. If the task is already accepted, stop.
8. Never modify remote repositories, send messages, place trades or publish releases unless the user explicitly authorized those external actions.
