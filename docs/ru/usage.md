# Использование

Запускайте команды из корня репозитория. CLI читает и записывает UTF-8, а для stdout/stderr использует UTF-8 на поддерживающих это текстовых потоках. Он обращается только к явно указанным путям. У него нет сетевого доступа, запуска shell-команд, вызова модели или телеметрии.

## Создать, проверить и скомпилировать контракт

```console
python src/scope_anchor.py new --out TASK.md --title "Исправить экспорт" --goal "Сохранить Unicode в экспортируемых данных"
python src/scope_anchor.py check TASK.md --json
python src/scope_anchor.py compile TASK.md
```

`new` создаёт незаполненный шаблон и отказывается перезаписывать существующий файл. `check` требует все одиннадцать разделов и отклоняет отсутствующие, пустые, повторные и неизвестные разделы, а также содержимое с `TODO`. `compile` прекращает работу при ошибках и выводит ограниченный запрос в stdout; перенаправление вывода — явное действие вызывающего shell.

## Сохранить локальные решения

```console
python src/scope_anchor.py lock --file .scope-anchor/decisions.json --key editor.format --value "Использовать форматтер репозитория"
python src/scope_anchor.py decisions --file .scope-anchor/decisions.json
python src/scope_anchor.py compile TASK.md --decisions .scope-anchor/decisions.json
python src/scope_anchor.py unlock --file .scope-anchor/decisions.json --key editor.format
```

Для намеренного изменения ключа укажите `--replace`. `decisions` показывает ключи и области действия, но не значения. Не сохраняйте в решениях секреты, учётные данные, приватный текст задач или персональные сведения. `.scope-anchor/` по умолчанию исключена из Git.

## Пути Windows и Ubuntu

PowerShell, путь с пробелами:

```powershell
py -3 src/scope_anchor.py new --out "рабочая папка/TASK.md" --goal "Проверить UTF-8"
```

Ubuntu:

```bash
python3 src/scope_anchor.py new --out 'рабочая папка/TASK.md' --goal 'Проверить UTF-8'
```

Для `new` родительская папка должна существовать. Кавычки передают путь как один аргумент.
