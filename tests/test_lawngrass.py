import pytest

from src.create_class import Product
from src.lawngrass_class import LawnGrass


@pytest.fixture
def sample_lawn_grass():
    """Фикстура для создания тестового объекта газонной травы."""
    return LawnGrass(
        name="Газонная трава",
        description="Мягкая",
        price=19.99,
        quantity=100,
        country="Россия",
        germination_period="2 недели",
        color="Зеленый",
    )


def test_lawn_grass_initialization(sample_lawn_grass):
    """Тест корректности инициализации газонной травы."""
    assert sample_lawn_grass.name == "Газонная трава"
    assert sample_lawn_grass.description == "Мягкая"  # Исправлено на "Мягкая"
    assert sample_lawn_grass.price == 19.99
    assert sample_lawn_grass.quantity == 100
    assert sample_lawn_grass.country == "Россия"
    assert sample_lawn_grass.germination_period == "2 недели"
    assert sample_lawn_grass.color == "Зеленый"


def test_lawn_grass_str_representation(sample_lawn_grass):
    """Тест строкового представления газонной травы."""
    expected_str = "Газонная трава, Россия, Зеленый, 19.99 руб. " "Остаток: 100 шт."
    assert str(sample_lawn_grass) == expected_str


def test_lawn_grass_inheritance():
    """Тест, что LawnGrass является наследником Product."""
    assert issubclass(LawnGrass, Product)


def test_lawn_grass_addition(sample_lawn_grass):
    """Тест сложения двух объектов газонной травы."""
    grass2 = LawnGrass(
        name="Трава Elite",
        description="Премиум качество",
        price=29.99,
        quantity=50,
        country="Германия",
        germination_period="3 недели",
        color="Темно-зеленый",
    )
    total = sample_lawn_grass + grass2
    assert total == (19.99 * 100) + (29.99 * 50)  # 1999 + 1499.5 = 3498.5


def test_lawn_grass_invalid_addition(sample_lawn_grass):
    """Тест попытки сложения с объектом другого класса."""

    class OtherProduct:
        pass

    other = OtherProduct()
    with pytest.raises(TypeError) as exc_info:
        sample_lawn_grass + other

    assert "Можно складывать только объекты класса Product" in str(exc_info.value)
