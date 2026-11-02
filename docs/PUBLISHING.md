# Release and publication

Releases use micro versions from `VERSION`. Before publishing, confirm the working tree and diff, run the checks in `docs/en/development.md`, inspect the staged tree and history for private data, and verify that the release notes match the tested code.

This project does not publish automatically. GitHub CI runs on pushes to `main` and pull requests; a successful local run is not a GitHub-hosted result. Do not create a GitHub Release or tag unless the version, commit contents, and checks have been verified. Use a normal push only when explicitly authorized; never force-push.

Repository description and topics are GitHub metadata, not files in this repository. Their desired values are documented in the release task and should be verified on the repository after any authorized update.

## Repository card metadata

Description:

> Native Codex skill for structured engineering tasks, reproducible workflows and quota-aware execution.

Topics: `codex`, `agent-skills`, `prompt-engineering`, `developer-tools`, `python`, `devsecops`, `workflow-automation`.

GitHub allows up to 20 topics; these seven use lowercase letters and hyphens and are within the documented 50-character limit. See [GitHub's topic guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics).
