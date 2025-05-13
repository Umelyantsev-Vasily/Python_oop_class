import pytest
from typing import Set, List
from src.create_class import Product, Category  # Замените `your_module` на имя вашего модуля


class TestCategoryInitialization:
    def test_init_empty_products(self):
        """Проверка инициализации категории с пустым списком продуктов."""
        category = Category(name="Тестовая категория", description="Описание")

        assert category.name == "Тестовая категория"
        assert category.description == "Описание"
        assert len(category.products) == 0
        assert Category.counting_categories >= 1  # Категория добавилась в счётчик

    def test_init_with_products(self):
        """Проверка инициализации категории с указанными продуктами."""
        product1 = Product("Товар 1", "Описание 1", 100.0, 10)
        product2 = Product("Товар 2", "Описание 2", 200.0, 5)

        category = Category(
            name="Категория с товарами",
            description="Описание",
            products=[product1, product2]
        )

        assert len(category.products) == 2
        assert product1 in category.products
        assert product2 in category.products

    def test_category_counter_increases(self):
        """Проверка, что счётчик категорий увеличивается при создании новой категории."""
        initial_count = Category.counting_categories

        category = Category(name="Новая категория", description="Описание")

        assert Category.counting_categories == initial_count + 1

    def test_unique_products_counter(self):
        """Проверка подсчёта уникальных товаров."""
        # Сбросим счётчики и множество товаров для чистоты теста
        Category.counting_categories = 0
        Category.all_products = set()
        Category.total_unique_products = 0

        product1 = Product("Уникальный товар 1", "Описание", 100.0, 5)
        product2 = Product("Уникальный товар 2", "Описание", 200.0, 3)

        # Создаём категорию с двумя уникальными товарами
        category1 = Category(
            name="Категория 1",
            description="Описание",
            products=[product1, product2]
        )

        assert Category.total_unique_products == 2

        # Создаём вторую категорию с одним новым и одним повторяющимся товаром
        product3 = Product("Уникальный товар 3", "Описание", 300.0, 2)
        category2 = Category(
            name="Категория 2",
            description="Описание",
            products=[product1, product3]  # product1 уже был в category1
        )

        assert Category.total_unique_products == 3
