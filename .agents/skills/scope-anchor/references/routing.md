# Advisory model and budget routing

No runtime detection or auto-switching. User choice and the **currently usable selected model** win over the table. Model names/availability may change; check the live Codex selector when it matters.

Default recommendation for ordinary multi-step engineering work: **GPT-6 Luna, Medium**. Recommend Low for simple editorial or mechanical changes. Recommend High only when task complexity or the cost of error gives a concrete reason; task length alone is not evidence. These are advisory defaults, not claims about the current selected model or a quota percentage.

| Task | Default advice | Escalate only if |
|---|---|---|
| Rename, docs, obvious one-file edit | Luna, Low | Evidence that reasoning is needed |
| Bounded code implementation and tests | Luna, Medium | Significant ambiguity / risk |
| UI or Windows-native integration | Selected model; Terra, Medium as alternative | Real integration needs it |
| Cross-layer root-cause investigation | Sol, Medium, if proven complex | Reproducible failure remains unresolved |
| High-risk security or concurrency | Selected capable model, High if warranted | Clearly justified by risk |

Default to one executor and targeted tool calls. No benchmark theatre or multiple parallel implementations merely to save usage. Keep sufficient quota for finish/verification; if percent unknown, say `QUOTA UNKNOWN`. Do not confuse Codex weekly limit, Codex 5-hour limit and gateway-provider allowances. No paid API use or hidden fallback. Local Ollama models are not assumed available just because they are configured.

Source of truth for model choice is the user's current selected configuration, **not** this document. Any recommendation is advisory and never a STOP gate.
