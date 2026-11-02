# Разработка

## Требования

Python 3.10+; сторонние зависимости не нужны. Проект рассчитан на Windows и Ubuntu. В CI используется Python 3.10 и 3.13 на обеих ОС.

## Проверки

```console
python -m unittest discover -s tests -v
python -m compileall -q src
python src/scope_anchor.py check examples/complete-task.md --json
python src/scope_anchor.py compile examples/complete-task.md
git diff --check
```

В Windows при необходимости используйте `py -3`, в Ubuntu — `python3`. Тесты включают CLI в отдельном процессе и полный цикл чтения/записи файла решений. Локальный тест не подтверждает успешный GitHub-hosted CI.

## Правила изменений

Сохраняйте офлайн-работу и стандартную библиотеку. Обновляйте английскую страницу и её русскую пару одним изменением. Закрепляйте Actions проверенными полными SHA, сохраняйте только чтение для `GITHUB_TOKEN` и ограничивайте время CI. Не включайте частные данные пользователя в примеры и логи.

См. [правила участия](../../CONTRIBUTING.ru.md) и [заметки о тестировании](../TESTING.md).
