import os
from pathlib import Path


def get_project_structure(startpath, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                # Пропускаем файлы миграций и кэша
                if ('migrations' not in root) and ('__pycache__' not in root):
                    # Пропускаем .pyc файлы и временные файлы
                    if not file.endswith(('.pyc', '.tmp', '.swp')):
                        f.write('{}{}\n'.format(subindent, file))


if __name__ == "__main__":
    project_path = input("Введите путь к Django проекту: ")
    output_file = "project_structure.txt"

    # Проверяем, что путь существует
    if not os.path.exists(project_path):
        print("Указанный путь не существует!")
        exit(1)

    # Проверяем, что это Django проект (ищем manage.py)
    if not os.path.isfile(os.path.join(project_path, 'manage.py')):
        print("Указанный путь не является Django проектом (не найден manage.py)!")
        exit(1)

    get_project_structure(project_path, output_file)
    print(f"Структура проекта сохранена в файл: {output_file}")