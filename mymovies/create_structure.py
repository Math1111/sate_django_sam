import os


def create_directory_structure(base_path, structure):
    """
    Создает структуру каталогов и файлов

    :param base_path: Базовый путь, где будет создана структура
    :param structure: Словарь, описывающий структуру
                     (ключи - имена каталогов/файлов, значения - содержимое или вложенная структура)
    """
    for name, content in structure.items():
        path = os.path.join(base_path, name)

        if isinstance(content, dict):
            # Это каталог с вложенной структурой
            os.makedirs(path, exist_ok=True)
            create_directory_structure(path, content)
        else:
            # Это файл
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content if content is not None else '')


# Пример структуры
directory_structure = {
    "project": {
        "src": {
            "main.py": "print('Hello, World!')",
            "utils.py": "# Utility functions",
            "__init__.py": None
        },
        "tests": {
            "test_main.py": "# Test cases",
            "__init__.py": None
        },
        "docs": {
            "README.md": "# Project Documentation",
            "requirements.txt": "python>=3.8\nnumpy\npandas"
        },
        ".gitignore": "*.pyc\n__pycache__/\n*.log",
        "LICENSE": None
    }
}

# Создаем структуру в текущей директории
create_directory_structure('.', directory_structure)

print("Структура каталогов и файлов успешно создана!")