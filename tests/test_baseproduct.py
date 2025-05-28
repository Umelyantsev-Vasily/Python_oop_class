from typing import Dict

import pytest

from src.base_product import BaseProduct


class TestBaseProduct:
    """Тесты для абстрактного базового класса BaseProduct"""

    def test_is_abstract(self):
        """Проверка, что класс действительно абстрактный"""
        with pytest.raises(TypeError):
            # Попытка создать экземпляр абстрактного класса
            BaseProduct("Test", "Description", 100.0, 5)

    def test_abstract_methods_exist(self):
        """Проверка наличия всех абстрактных методов"""
        assert "__init__" in BaseProduct.__abstractmethods__
        assert "__str__" in BaseProduct.__abstractmethods__
        assert "price" in BaseProduct.__abstractmethods__
        assert "new_product" in BaseProduct.__abstractmethods__

    def test_abstract_methods_signatures(self):
        """Проверка сигнатур абстрактных методов"""
        # Проверка сигнатуры __init__
        init_method = BaseProduct.__init__.__annotations__
        assert init_method["name"] == str
        assert init_method["description"] == str
        assert init_method["price"] == float
        assert init_method["quantity"] == int

        # Проверка сигнатуры __str__
        str_method = BaseProduct.__str__.__annotations__
        assert str_method["return"] == str

        # Проверка сигнатуры price (property)
        assert isinstance(BaseProduct.price, property)

        # Проверка сигнатуры new_product
        new_product_method = BaseProduct.new_product.__annotations__
        # Исправленная проверка для Python 3.9+ (можно использовать любой вариант)
        assert new_product_method["product_data"] in (Dict, dict)  # Оба варианта допустимы
        assert new_product_method["return"] == "BaseProduct"

    def test_concrete_implementation(self):
        """Проверка работы конкретной реализации"""

        class ConcreteProduct(BaseProduct):
            def __init__(self, name: str, description: str, price: float, quantity: int):
                self.name = name
                self.description = description
                self._price = price
                self.quantity = quantity

            def __str__(self) -> str:
                return f"{self.name} - {self.description}"

            @property
            def price(self) -> float:
                return self._price

            @classmethod
            def new_product(cls, product_data: Dict) -> "ConcreteProduct":
                return cls(**product_data)

        # Тестирование конкретной реализации
        product = ConcreteProduct("Test", "Desc", 100.0, 5)
        assert product.name == "Test"
        assert product.description == "Desc"
        assert product.price == 100.0
        assert product.quantity == 5
        assert str(product) == "Test - Desc"

        # Тестирование фабричного метода
        product_data = {"name": "FromFactory", "description": "FactoryDesc", "price": 200.0, "quantity": 10}
        factory_product = ConcreteProduct.new_product(product_data)
        assert factory_product.name == "FromFactory"
