# Supported project stack

ScopeAnchor's implementation uses Python 3.10+ and the standard library only. The primary integration is a native Agent Skill under `.agents/skills/scope-anchor/`; the CLI is optional. Documentation and examples use Markdown and JSON. GitHub Actions provides CI on Windows and Ubuntu. Russian companion: [docs/ru/stack.md](ru/stack.md).

The skill is intended for Codex environments that discover project-level `.agents/skills/` folders. Exact discovery and activation depend on the host environment and are not guaranteed by the CLI. ScopeAnchor does not install itself, alter Codex settings, call a model, or require a hosted service.

The CLI accepts explicit file paths and has no shell, network, database, or third-party runtime dependency. See [architecture](en/architecture.md) and [security](../SECURITY.md).
