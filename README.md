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
Python_oop_class/
├── data/                  # Папка с данными (если используется)
├── htmlcov/              # Отчеты coverage в HTML
├── src/
│   ├── __init__.py       # Пакетный файл
│   ├── create_class.py   # Основные классы (Product, Category)
│   ├── lawngrass_class.py # Класс LawnGrass
│   ├── smartphone_class.py # Класс Smartphone
│   ├── read.json.py      # Функции для работы с JSON
│   └── main.py           # Точка входа
├── tests/
│   ├── __init__.py
│   ├── conftest.py       # Фикстуры pytest
│   ├── test_create_class.py # Тесты для основных классов
│   ├── test_lawngrass.py # Тесты для LawnGrass
│   ├── test_read.json.py # Тесты для работы с JSON
│   ├── test_smartphone_class.py # Тесты для Smartphone
│   └── coverage/         # Результаты тестового покрытия
├── .coverage             # Файл coverage
├── .flake8               # Конфиг flake8
├── .gitignore            # Игнорируемые файлы
├── poetry.lock           # Файл блокировки Poetry
└── pyproject.toml        # Конфигурация проекта
```
----
## 🧩 Основной функционал

### Базовые классы
- `Product` - базовый класс товара
- `Category` - класс категорий товаров

### Новый функционал

#### 🆕 Специализированные классы товаров
1. **`Smartphone`**:
   - Производительность (`efficiency`)
   - Модель (`model`)
   - Объем памяти (`memory`)
   - Цвет (`color`)

2. **`LawnGrass`**:
   - Страна-производитель (`country`)
   - Срок прорастания (`germination_period`)
   - Цвет (`color`)

#### 🔒 Защищенные операции
- Проверка типов при добавлении в категорию
- Защита от некорректных цен (только положительные значения)
- Ограничение сложения товаров одного типа

#### ➕ Новые возможности
```python
# Сложение стоимости товаров одного типа
total = smartphone1 + smartphone2

# Защищенное добавление в категорию
try:
    category.add_product("не товар")
except TypeError as e:
    print(e)
```
---
## Реализованная функциональность

- Базовый абстрактный класс Product
- Миксин для логирования создания объектов
- Специализированные классы товаров
- Сложение товаров по стоимости
- Управление категориями
---
## 🧪 Покрытие тестами: 
```
Name                                Stmts   Miss  Cover
-------------------------------------------------------
src\__init__.py                         0      0   100%
src\base_product.py                    15      3    80%
src\create_class.py                    94     20    79%
src\creationloggermixin.py             15      0   100%
src\lawngrass_class.py                  9      0   100%
src\read_json.py                       14      0   100%
src\smartphone_class.py                18      0   100%
tests\__init__.py                       0      0   100%
tests\conftest.py                      22      3    86%
tests\test_baseproduct.py              48      0   100%
tests\test_creationloggermixin.py      44      0   100%
tests\test_creete_class.py            135      0   100%
tests\test_lawngrass.py                30      0   100%
tests\test_read_json.py                32      0   100%
tests\test_smartphone_class.py         33      0   100%
-------------------------------------------------------
TOTAL                                 509     26    95%



```
---
## 📝 Лицензия
Проект распространяется под [лицензией MIT](LICENSE)
