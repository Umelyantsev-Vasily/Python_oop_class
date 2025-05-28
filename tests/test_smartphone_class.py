import pytest

from src.create_class import Product
from src.smartphone_class import Smartphone


def test_smartphone_initialization(sample_smartphone):
    """Тест корректности инициализации смартфона """
    assert sample_smartphone.name == "iPhone 15"
    assert sample_smartphone.description == "Флагман"
    assert sample_smartphone.price == 999.99
    assert sample_smartphone.quantity == 5
    assert sample_smartphone.efficiency == "High"
    assert sample_smartphone.model == "15 Pro"
    assert sample_smartphone.memory == "256GB"
    assert sample_smartphone.color == "Black"


def test_smartphone_str_representation(sample_smartphone):
    """Тест строкового представления смартфона """
    expected_str = "iPhone 15, 15 Pro, Black, 999.99 руб. Остаток: 5 шт."
    assert str(sample_smartphone) == expected_str


def test_smartphone_inheritance():
    """Тест наследования от класса Product """
    assert issubclass(Smartphone, Product)


def test_smartphone_addition(sample_smartphone):
    """Тест сложения двух смартфонов """
    smartphone2 = Smartphone(
        name="Samsung Galaxy",
        description="Андроид флагман",
        price=899.99,
        quantity=3,
        efficiency="Высокая",
        model="S23 Ultra",
        memory="512GB",
        color="White",
    )
    total = sample_smartphone + smartphone2
    assert total == (999.99 * 5) + (899.99 * 3)  # 4999.95 + 2699.97 = 7699.92


def test_smartphone_invalid_addition(sample_smartphone):
    """Тест попытки сложения с объектом другого класса"""

    class OtherProduct:
        pass

    other = OtherProduct()
    with pytest.raises(TypeError) as exc_info:
        sample_smartphone + other

    assert "Можно складывать только объекты класса Product" in str(exc_info.value)


def test_smartphone_price_setter(sample_smartphone):
    """Тест изменения цены смартфона"""
    sample_smartphone.price = 1099.99
    assert sample_smartphone.price == 1099.99

    # Проверка на отрицательную цену
    with pytest.raises(ValueError):
        sample_smartphone.price = -100
