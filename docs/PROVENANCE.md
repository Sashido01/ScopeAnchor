# Provenance and licensing

ScopeAnchor is an independent implementation of a structured task contract for native Codex skills.

The project was informed by the general ideas of auditing task prompts and recording decisions in [Jakeschincariol/promptmaster-skill](https://github.com/Jakeschincariol/promptmaster-skill), licensed under MIT. That project targets Claude; ScopeAnchor targets native Codex skills. ScopeAnchor does not copy its source code, skill text, 35-rule catalog, or contradiction-blocking behavior. Its code, documentation, CLI, and tests were written independently. This attribution does not imply endorsement or participation by that author.

Methodology references include official OpenAI material on [skills](https://developers.openai.com/plugins/concepts/skills), [building focused skills](https://developers.openai.com/plugins/build/skills), [progressive disclosure](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), and [Codex workflows](https://developers.openai.com/blog/skills-agents-sdk). These sources support keeping the skill entry point concise and loading detailed references only when useful; they do not establish a measured quota reduction. No third-party library source is vendored. The project license is MIT; see [LICENSE](../LICENSE).
