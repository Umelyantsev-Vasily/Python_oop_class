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

    def test_init_with_products(self):
        """Проверка инициализации категории с указанными продуктами."""
        product1 = Product("Товар 1", "Описание 1", 100.0, 10)
        product2 = Product("Товар 2", "Описание 2", 200.0, 5)

        category = Category(name="Категория с товарами", description="Описание", products=[product1, product2])

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
        category1 = Category(name="Категория 1", description="Описание", products=[product1, product2])

        assert Category.total_unique_products == 2

        # Создаём вторую категорию с одним новым и одним повторяющимся товаром
        product3 = Product("Уникальный товар 3", "Описание", 300.0, 2)
        category2 = Category(
            name="Категория 2", description="Описание", products=[product1, product3]  # product1 уже был в category1
        )

        assert Category.total_unique_products == 3


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


class TestExistingFunctionality:
    """Тесты для проверки, что старая функциональность продолжает работать"""

    def test_category_init_with_products(self):
        """Проверка инициализации категории с продуктами (старый тест)"""
        product = Product("Товар", "Описание", 100.0, 5)
        category = Category("Категория", "Описание", [product])

        assert len(category.products) == 1
        assert product in category.products

    def test_product_creation(self):
        """Проверка создания продукта (старый тест)"""
        product = Product("Товар", "Описание", 100.0, 5)
        assert product.name == "Товар"
        assert product.description == "Описание"
        assert product.quantity == 5
