import unittest

import pytest

from src.create_class import Category, Product
from src.lawngrass_class import LawnGrass
from src.smartphone_class import Smartphone


class TestProductAddition:
    """Тесты для новой функциональности сложения продуктов"""

    def test_product_addition(self):
        """Проверка корректного сложения двух продуктов"""
        p1 = Product("iPhone 15", "128GB, черный", 79990.0, 5)
        p2 = Product("Samsung Galaxy S23", "256GB, синий", 74990.0, 3)
        total = p1 + p2
        assert total == 79990.0 * 5 + 74990.0 * 3

    def test_product_addition_with_different_types(self):
        """Проверка попытки сложения с объектом другого типа"""
        p1 = Product("Xiaomi Redmi Note 12", "128GB, серый", 21990.0, 10)

        with pytest.raises(TypeError) as excinfo:
            result = p1 + "не продукт"
        assert "Можно складывать только объекты класса Product" in str(excinfo.value)

    def test_multiple_additions(self):
        """Проверка последовательного сложения нескольких продуктов"""
        p1 = Product("Realme 10", "128GB, белый", 18990.0, 2)
        p2 = Product("Honor 90", "256GB, зеленый", 39990.0, 3)
        p3 = Product("OnePlus 11", "256GB, черный", 64990.0, 4)

        # Складываем общие стоимости каждого продукта
        total = p1.total_cost() + p2.total_cost() + p3.total_cost()
        assert total == 18990.0 * 2 + 39990.0 * 3 + 64990.0 * 4


class TestCategoryInitialization:
    """Тесты инициализации категории"""

    def test_init_empty_products(self):
        category = Category(name="Смартфоны", description="Мобильные устройства")
        assert category.name == "Смартфоны"
        assert category.description == "Мобильные устройства"
        assert len(category.products) == 0
        assert Category.counting_categories >= 1

    def test_category_counter_increases(self):
        initial_count = Category.counting_categories
        category = Category(name="Умные часы", description="Гаджеты для фитнеса")
        assert Category.counting_categories == initial_count + 1


class TestProductPrice:
    """Тесты работы с ценой продукта"""

    def test_price_getter(self):
        product = Product("Nokia G22", "128GB, синий", 17990.0, 5)
        assert product.price == 17990.0

    def test_price_setter_valid(self):
        product = Product("Motorola Edge 40", "256GB, черный", 44990.0, 5)
        product.price = 39990.0
        assert product.price == 39990.0

    def test_price_setter_invalid(self):
        product = Product("Tecno Camon 20", "128GB, золотой", 15990.0, 5)

        # Проверяем, что цена не меняется при невалидных значениях
        product.price = 0
        assert product.price == 15990.0

        product.price = -50.0
        assert product.price == 15990.0

    def test_private_price_access(self):
        product = Product("Infinix Note 30", "256GB, серебристый", 19990.0, 5)
        with pytest.raises(AttributeError):
            _ = product.__price


class TestProductCreation:
    """Тесты создания продукта"""

    def test_product_creation(self):
        product = Product("Vivo Y36", "128GB, фиолетовый", 22990.0, 5)
        assert product.name == "Vivo Y36"
        assert product.description == "128GB, фиолетовый"
        assert product.quantity == 5


class TestCategoryProducts(unittest.TestCase):
    """Тесты работы с продуктами в категориях"""

    @classmethod
    def setUpClass(cls):
        Category.counting_categories = 0
        Category.total_unique_products = 0
        Category.all_products = set()

    def test_add_product(self):
        c = Category("Смартфоны", "Мобильные устройства")
        p = Product("Oppo Reno 10", "256GB, голубой", 39990.0, 10)
        c.add_product(p)
        self.assertEqual(len(c), 10)
        self.assertIn(p, Category.all_products)

    def test_add_invalid_product(self):
        c = Category("Планшеты", "Мобильные компьютеры ")
        with self.assertRaises(TypeError):
            c.add_product("not a product")

    def test_add_zero_quantity_product(self):
        c = Category("Аксессуары", "Чехлы и защитные стекла ")
        p_zero = Product("Чехол для iPhone", "Силиконовый, черный", 990.0, 0)
        c.add_product(p_zero)
        self.assertEqual(len(c), 0)  # Продукт не должен добавиться


class TestCategoryCounters(unittest.TestCase):
    """Тесты счетчиков категорий"""

    @classmethod
    def setUpClass(cls):
        Category.counting_categories = 0
        Category.total_unique_products = 0
        Category.all_products = set()

    def test_counters(self):
        initial_categories = Category.counting_categories
        initial_products = Category.total_unique_products

        p1 = Product("iPhone 14 Pro", "256GB, золотой", 99990.0, 5)
        p2 = Product("Samsung Z Flip5", "512GB, фиолетовый", 109990.0, 3)
        title = Category("Флагманы", "Топовые модели", [p1, p2])

        self.assertEqual(Category.counting_categories, initial_categories + 1)
        self.assertEqual(Category.total_unique_products, initial_products + 2)


def test_add_smartphones():
    """Сложение двух смартфонов (успешно)"""
    phone1 = Smartphone("iPhone", "Флагман", 1000, 2, "High", "15", "256GB", "Black")
    phone2 = Smartphone("Samsung", "Флагман", 900, 3, "High", "S23", "512GB", "White")
    total = phone1 + phone2
    assert total == (1000 * 2) + (900 * 3)  # 2000 + 2700 = 4700


def test_add_lawn_grasses():
    """Сложение двух видов травы (успешно)."""
    grass1 = LawnGrass("Трава", "Мягкая", 20, 50, "Россия", "2 недели", "Зеленый")
    grass2 = LawnGrass("Трава Premium", "Мягкая", 30, 40, "Германия", "3 недели", "Зеленый")
    total = grass1 + grass2
    assert total == (20 * 50) + (30 * 40)  # 1000 + 1200 = 2200


def test_add_different_classes():
    """Попытка сложить смартфон и траву (ошибка TypeError)."""
    phone = Smartphone("iPhone", "Флагман", 1000, 2, "High", "15", "256GB", "Black")
    grass = LawnGrass("Трава", "Мягкая", 20, 50, "Россия", "2 недели", "Зеленый")
    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        total = phone + grass
