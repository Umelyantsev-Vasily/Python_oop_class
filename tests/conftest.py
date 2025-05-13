import pytest

from src.create_class import Category, Product


# @pytest.fixture
# def sample_product():
#     return Product("Телефон", "Смартфон", 50000.0, 10)
#

# @pytest.fixture
# def sample_products():
#     return [Product("Телефон", "Смартфон", 50000.0, 10), Product("Ноутбук", "Игровой", 100000.0, 5)]


# @pytest.fixture
# def sample_category(sample_products):
#     return Category("Электроника", "Техника", sample_products)
#
#
@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасываем счётчики перед каждым тестом"""
    Category.counting_categories = 0
    Category.total_unique_products = 0
    Category._all_products = set()
    yield
