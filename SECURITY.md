# Security policy

## Supported version

Security fixes are prepared for the latest version on the `main` branch. There is no separate long-term support branch or service-level response commitment.

## Report a vulnerability

Use [GitHub's private vulnerability reporting form](https://github.com/Sashido01/ScopeAnchor/security/advisories/new). Include the affected version or commit, impact, and concise reproduction steps. Avoid sending real secrets or unrelated personal data. Do not report exploitable details in public Issues or Pull Requests.

If GitHub reports that private vulnerability reporting is unavailable, do not publish exploit details. Use the repository's Security page to check for an alternative private reporting path; do not assume an email address or response deadline that is not published.

Reports are reviewed as maintainer time permits. No acknowledgment or fix timeline is guaranteed. Coordinated disclosure is appreciated.

## Scope

The CLI is an offline helper, not a security boundary. It does not run task text, but users remain responsible for reviewing contracts before sharing or compiling them. See [the security guide](docs/en/troubleshooting.md#security-and-data).
