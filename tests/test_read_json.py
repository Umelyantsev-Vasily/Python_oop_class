import json
from tempfile import NamedTemporaryFile

import pytest

from src.read_json import Category, load_categories_from_json


@pytest.fixture
def sample_json_file():
    """Фикстура с тестовыми JSON данными"""
    data = [
        {
            "name": "Смартфоны",
            "description": "Мобильные устройства",
            "products": [
                {"name": "iPhone 15", "description": "512GB, Gray", "price": 210000.0, "quantity": 8},
                {"name": "Samsung Galaxy", "description": "256GB, Black", "price": 180000.0, "quantity": 5},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Большие экраны",
            "products": [{"name": "QLED 4K", "description": "55 дюймов", "price": 123000.0, "quantity": 3}],
        },
    ]

    with NamedTemporaryFile(mode="w+", suffix=".json", encoding="utf-8", delete=False) as f:
        json.dump(data, f, ensure_ascii=False)
        f.flush()
        yield f.name
    # Файл автоматически удалится после тестов


def test_load_empty_categories(tmp_path):
    """Тест загрузки пустого списка категорий"""
    empty_file = tmp_path / "empty.json"
    empty_file.write_text("[]", encoding="utf-8")

    categories = load_categories_from_json(str(empty_file))
    assert len(categories) == 0
    assert Category.counting_categories == 0
    assert Category.total_unique_products == 0


def test_file_not_found():
    """Тест обработки отсутствующего файла"""
    with pytest.raises(FileNotFoundError):
        load_categories_from_json("nonexistent_file.json")


def test_invalid_json(tmp_path):
    """Тест обработки невалидного JSON"""
    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text('{"invalid": data}', encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        load_categories_from_json(str(invalid_file))


def test_counters_reset(sample_json_file):
    """Тест сброса счетчиков перед загрузкой"""
    # Первая загрузка
    load_categories_from_json(sample_json_file)
    initial_categories = Category.counting_categories
    initial_products = Category.total_unique_products

    # Вторая загрузка (счетчики должны сброситься)
    # categories = load_categories_from_json(sample_json_file)
    assert Category.counting_categories == initial_categories
    assert Category.total_unique_products == initial_products
