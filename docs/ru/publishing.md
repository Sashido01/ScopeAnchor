# Релиз и публикация

Версии задаются файлом `VERSION` и увеличиваются микрошагом. Перед публикацией проверьте рабочее дерево и diff, выполните проверки из [руководства по разработке](development.md), изучите staged tree и историю на предмет частных данных, сверьте release notes с проверенным кодом.

Автоматической публикации в проекте нет. GitHub CI запускается при push в `main` и для Pull Request; локальный успешный запуск не является результатом GitHub-hosted CI. Не создавайте Release или tag, пока версия, содержимое commit и проверки не подтверждены. Используйте обычный push только при явном разрешении; не выполняйте force-push.

Description и topics — метаданные GitHub, а не файлы этого репозитория. После разрешённого изменения проверьте их значение непосредственно в карточке репозитория.

## Метаданные карточки

Description:

> Native Codex skill for structured engineering tasks, reproducible workflows and quota-aware execution.

Topics: `codex`, `agent-skills`, `prompt-engineering`, `developer-tools`, `python`, `devsecops`, `workflow-automation`.

GitHub допускает до 20 topics; эти семь используют строчные буквы и дефисы, каждое название короче 50 символов. См. [правила GitHub для topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics).
