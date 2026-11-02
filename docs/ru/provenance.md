# Происхождение и лицензии

ScopeAnchor — самостоятельная реализация контракта инженерной задачи для нативных Codex skills.

На общие идеи аудита запросов и сохранения решений повлиял [Jakeschincariol/promptmaster-skill](https://github.com/Jakeschincariol/promptmaster-skill) под лицензией MIT. Этот проект предназначен для Claude, а ScopeAnchor — для нативных Codex skills. ScopeAnchor не копирует его исходный код, текст skill, каталог из 35 правил или поведение блокировки при противоречиях. Код, документация, CLI и тесты ScopeAnchor созданы самостоятельно. Указание источника не означает одобрения или участия автора.

Источники методологии — официальные материалы OpenAI:

- [Skills](https://developers.openai.com/plugins/concepts/skills)
- [Building skills](https://developers.openai.com/plugins/build/skills)
- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
- [Using skills and GitHub Actions to optimize Codex workflows](https://developers.openai.com/blog/skills-agents-sdk)

Эти источники обосновывают краткую точку входа skill и загрузку подробных материалов по необходимости; они не подтверждают измеренное снижение расхода квоты.

Исходный код сторонних библиотек не включён. Лицензия проекта — MIT, см. [LICENSE](../../LICENSE).
