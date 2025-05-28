import pytest

from src.create_class import Category, Product
from src.lawngrass_class import LawnGrass
from src.smartphone_class import Smartphone


@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасываем счётчики перед каждым тестом"""
    Category.counting_categories = 0
    Category.total_unique_products = 0
    Category._all_products = set()
    yield


@pytest.fixture
def sample_product() -> Product:
    return Product("Книга", "Интересная книга", 500, 10)


@pytest.fixture
def sample_smartphone() -> Smartphone:
    return Smartphone("iPhone 15", "Флагман", 999.99, 5, "High", "15 Pro", "256GB", "Black")


@pytest.fixture
def sample_lawn_grass() -> LawnGrass:
    return LawnGrass("Газонная трава", "Мягкая", 19.99, 100, "Россия", "2 недели", "Зеленый")


@pytest.fixture
def sample_category():
    return Category("Техника", "Электроника")
