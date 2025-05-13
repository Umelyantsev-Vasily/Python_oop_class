import unittest
from typing import List, Set

import pytest

from src.create_class import Category, Product


class TestCategoryInitialization:
    def test_init_empty_products(self):
        """Проверка инициализации категории с пустым списком продуктов."""
        category = Category(name="Тестовая категория", description="Описание")

        assert category.name == "Тестовая категория"
        assert category.description == "Описание"
        assert len(category.products) == 0
        assert Category.counting_categories >= 1  # Категория добавилась в счётчик

    def test_category_counter_increases(self):
        """Проверка, что счётчик категорий увеличивается при создании новой категории."""
        initial_count = Category.counting_categories

        category = Category(name="Новая категория", description="Описание")

        assert Category.counting_categories == initial_count + 1


class TestProductPrice:
    """Тесты для новой функциональности работы с ценой продукта"""

    def test_price_getter(self):
        """Проверка корректности работы геттера цены"""
        product = Product("Тест", "Описание", 100.0, 5)
        assert product.price == 100.0  # Проверяем, что геттер возвращает правильное значение

    def test_price_setter_valid(self):
        """Проверка установки допустимой цены"""
        product = Product("Тест", "Описание", 100.0, 5)
        product.price = 150.0  # Устанавливаем новую цену
        assert product.price == 150.0  # Проверяем, что цена изменилась

    def test_price_setter_invalid(self, capsys):
        """Проверка реакции на недопустимую цену (<= 0)"""
        product = Product("Тест", "Описание", 100.0, 5)

        # Пробуем установить нулевую цену
        product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0  # Цена не должна измениться

        # Пробуем установить отрицательную цену
        product.price = -50.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0  # Цена не должна измениться

    def test_private_price_access(self):
        """Проверка, что цена действительно приватная"""
        product = Product("Тест", "Описание", 100.0, 5)
        with pytest.raises(AttributeError):
            # Пытаемся получить доступ к __price напрямую
            _ = product.__price

    def test_product_creation(self):
        """Проверка создания продукта (старый тест)"""
        product = Product("Товар", "Описание", 100.0, 5)
        assert product.name == "Товар"
        assert product.description == "Описание"
        assert product.quantity == 5


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )


class Category:
    counting_categories: int = 0
    total_unique_products: int = 0
    all_products: Set[Product] = set()

    def __init__(self, name: str, description: str, products: List[Product] = None):
        self.name = name
        self.description = description
        self.__products = []

        Category.counting_categories += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        if product.quantity <= 0:
            print("Товар с нулевым количеством не может быть добавлен")
            return

        self.__products.append(product)
        Category.total_unique_products += 1

        if product not in Category.all_products:
            Category.all_products.add(product)

    @property
    def products(self) -> str:
        products_info = ""
        for product in self.__products:
            products_info += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_info

    def __len__(self) -> int:
        return sum(product.quantity for product in self.__products)


class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        p = Product("Test", "Desc", 100.0, 10)
        self.assertEqual(p.name, "Test")
        self.assertEqual(p.description, "Desc")
        self.assertEqual(p.price, 100.0)
        self.assertEqual(p.quantity, 10)

    def test_price_setter(self):
        p = Product("Test", "Desc", 100.0, 10)

        # Test valid price
        p.price = 150.0
        self.assertEqual(p.price, 150.0)

        # Test invalid price (should print message but not change price)
        p.price = -50.0
        self.assertEqual(p.price, 150.0)

    def test_new_product_classmethod(self):
        data = {"name": "New", "description": "New desc", "price": 200.0, "quantity": 5}
        p = Product.new_product(data)
        self.assertIsInstance(p, Product)
        self.assertEqual(p.name, "New")


class TestCategory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Reset counters before tests
        Category.counting_categories = 0
        Category.total_unique_products = 0
        Category.all_products = set()

    def test_category_creation(self):
        c = Category("Test Cat", "Test Desc")
        self.assertEqual(c.name, "Test Cat")
        self.assertEqual(len(c), 0)

    def test_add_product(self):
        c = Category("Test Cat", "Test Desc")
        p = Product("Test", "Desc", 100.0, 10)

        # Test valid product
        c.add_product(p)
        self.assertEqual(len(c), 10)
        self.assertIn(p, Category.all_products)

        # Test invalid product (not Product instance)
        with self.assertRaises(TypeError):
            c.add_product("not a product")

        # Test zero quantity product
        p_zero = Product("Zero", "Desc", 100.0, 0)
        c.add_product(p_zero)  # Should print message but not raise exception
        self.assertEqual(len(c), 10)  # Quantity shouldn't change

    def test_products_property(self):
        p1 = Product("P1", "Desc", 100.0, 5)
        p2 = Product("P2", "Desc", 200.0, 3)
        c = Category("Test Cat", "Test Desc", [p1, p2])

        expected_output = "P1, 100.0 руб. Остаток: 5 шт.\nP2, 200.0 руб. Остаток: 3 шт.\n"
        self.assertEqual(c.products, expected_output)

    def test_counters(self):
        initial_categories = Category.counting_categories
        initial_products = Category.total_unique_products

        p1 = Product("P1", "Desc", 100.0, 5)
        p2 = Product("P2", "Desc", 200.0, 3)
        c = Category("Test Cat", "Test Desc", [p1, p2])

        self.assertEqual(Category.counting_categories, initial_categories + 1)
        self.assertEqual(Category.total_unique_products, initial_products + 2)
