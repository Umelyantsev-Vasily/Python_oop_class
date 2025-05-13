# 🐍 Python OOP Class Project

![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![Poetry](https://img.shields.io/badge/packaging-poetry-cyan.svg)
![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)
![Type Checked](https://img.shields.io/badge/types-mypy-blue.svg)
![Tests](https://img.shields.io/badge/tests-pytest-blue.svg)

Проект для изучения объектно-ориентированного программирования на Python.

## 📦 Зависимости

```
Python >= 3.13
Poetry (для управления зависимостями)
```
## 🛠️ Инструменты разработки
- Форматирование: black

- Линтинг: flake8

- Проверка типов: mypy

- Тестирование: pytest

- Сортировка импортов: isort
---
## ⚙️ Установка
1. Установите Poetry (если еще не установлен):
```
pip install poetry
```
2. Клонируйте репозиторий: 
```
https://github.com/Umelyantsev-Vasily/Python_oop_class/tree/develop
```
3. Установите зависимости:
```
poetry install
```
4. Активируйте виртуальное окружение:
```
poetry shell
```
---
## 📂 Структура проекта
```
python-oop-klass/
├── src/                   # Исходный код
│   └── create_class.py    # Основной модуль
├── tests/                 # Тесты
├── pyproject.toml         # Конфигурация проекта
└── README.md              # Этот файл
```
---
##  🧩Пакеты 
- [create_class.py](https://github.com/Umelyantsev-Vasily/Python_oop_class/blob/feature/class_14_1/src/create_class.py) -> Реализованны клвссы  
- [read_json.py](https://github.com/Umelyantsev-Vasily/Python_oop_class/blob/feature/class_14_1/src/read_json.py) -> Функция для чтения Json Файла 
---

## 🧪 Покрытие тестами: 
```
Name                         Stmts   Miss  Cover
------------------------------------------------
src\__init__.py                  0      0   100%
src\create_class.py             42      3    93%
src\main.py                     37     37     0%
src\read_json.py                14      0   100%
tests\__init__.py                0      0   100%
tests\conftest.py                8      0   100%
tests\test_creete_class.py      64      0   100%
tests\test_read_json.py         43      0   100%
------------------------------------------------
TOTAL                          208     40    81%
```
---
## 📝 Лицензия
Проект распространяется под [лицензией MIT](LICENSE)