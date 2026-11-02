# Task contract

Use the fields below internally, or explicitly in a handoff. Keep every item short; only facts supported by the user's request, the current repo, or observed tools.

| Field | Required meaning |
|---|---|
| `GOAL` | One concrete deliverable or problem to fix |
| `SCOPE` | Files/workstreams in scope, and intended effect |
| `NON-GOALS` | Work deliberately not requested |
| `CURRENT STATE` | Observed baseline + evidence; unknown if not inspected |
| `LOCKED SEMANTICS` | Confirmed choices not to re-litigate, subject to explicit updated user directions |
| `INVARIANTS` | Behavior, data, security and compatibility that must remain unchanged |
| `FILES` | Known relevant paths; avoid listing the entire repository |
| `ACCEPTANCE` | Observable criteria establishing completion |
| `TESTS` | Least-cost reproducible checks, plus mandatory project gates |
| `STOP` | Stop after acceptance, or state exact blocker; no invented expansion |
| `REPORT` | Status, changed files, proof, limitations, Git state |

Priority: platform safety and tool permissions → explicit latest user request → applicable repo instructions → previously locked decisions → generic skill suggestions. Conflicts between standing defaults and a new explicit user request are **not** a reason to block: identify the override, proceed if safe, and report meaningful updates. For forbidden external actions (push, deploy, orders, credential exposure), use the relevant actual approval boundary.

Avoid anti-patterns: whole-file dumps for one function, unverified assertions, repeated clarification loops, parallel model races, premature full-suite tests, wide refactors of a narrow bug, fabricated quotes, and turning missing metrics into claimed wins.
