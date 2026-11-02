---
name: scope-anchor
description: Turn a complex Codex coding task into a bounded, testable execution contract; preserve known project decisions, minimize retries, select advisory model effort, and finish with evidence. Use for multi-step implementation, debugging and DevSecMLOps work; not simple questions.
---

# ScopeAnchor — concise execution discipline

This is **guidance for the current task**, not a replacement for user instructions, Codex permissions, approval gates, or repo-specific `AGENTS.md`. Do not install anything or change any global config to use it. When the user requests execution, **execute**; do not return just a rewritten prompt.

1. Read applicable `AGENTS.md` and only relevant repository docs/files. Inspect `git status` before edits. Keep uncommitted user changes intact. Never blindly assume a Windows/Linux path, a model capability, or a quota percentage.
2. Identify the actual user request, existing progress, and the **one remaining deliverable**. If already complete, verify available evidence and report `COMPLETE`; do not invent a follow-up task. Separate `FACT`, `INFERENCE`, `UNKNOWN`.
3. Audit the request for repeated or conflicting instructions, missing acceptance criteria, unspecified stack/runtime, irrelevant context, and unjustified scope expansion. Resolve only from the request and repository evidence; carry essential unknowns forward without guessing. Keep the internal execution contract to the few details that matter: goal, scope and invariants, acceptance, checks, and stop condition. Do not enumerate the eleven-field template or create a separate contract/spec/plan/log by default. Read [references/task-contract.md](references/task-contract.md) when the user asks for a reusable contract or explicit handoff, or when the optional CLI is being used.
4. Read [references/routing.md](references/routing.md) only if model selection or quota is relevant. Treat routes as **advice**: the already selected usable model wins. Never block, restart, race models or switch models solely for a recommendation. Separate Codex weekly quota from gateway/Ollama limits. Minimize total accepted-task cost, not theoretical per-token price.
5. Implement by the **native** mechanism of the target project. Prefer reuse/adaptation under compatible licenses; no wrappers, hooks, shadow runtimes, unsupported APIs or magic proxies. For security-sensitive changes follow [references/verification.md](references/verification.md). Keep each change smallest meaningful and testable. Do not copy secrets or private paths into public artifacts.
6. Diagnose root cause before patches. Use targeted tests while iterating, project-mandated tests before completion. If attempts repeat without progress, reassess evidence and approach instead of looping blindly. Log real evidence in the project's established format; do not generate a new logging hierarchy unless needed.
7. Keep documentation accurate and local Git commits readable **when the user has authorized commits in this repository**. Never push, create PR, merge, overwrite uncommitted changes or publish artifacts without explicit user request. Existing repo-specific restrictions control.
8. End when the acceptance criteria are met. Final report: `STATUS: COMPLETE|PARTIAL|BLOCKED`, files and outcomes, observed tests, `NOT_VERIFIED`, local Git state and any bounded blocker. Do not invent new work just to keep the task open.

When asked to *prepare* a prompt rather than execute the task, output the contract only. When asked to *implement*, proceed without an extra confirmation step unless a real permission/security requirement applies. Don't claim any reduction in token spending without a measured before/after.

The optional Python helper at repository root (`src/scope_anchor.py`) can scaffold/validate/compile standalone contracts. It is **not** required for skill activation and must not be auto-run when unnecessary.
