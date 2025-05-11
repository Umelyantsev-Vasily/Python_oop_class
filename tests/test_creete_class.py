from src.create_class import Category, Product


def test_category_initialization():
    p1 = Product("Телефон", "Смартфон", 50000.0, 10)
    p2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    category = Category("Электроника", "Техника", [p1, p2])

    assert category.name == "Электроника"
    assert len(category.products) == 2
    assert Category.counting_categories == 1
    assert Category.total_unique_products == 2


def test_products_counting():
    # Сброс статических полей перед тестом
    Category.counting_categories = 0
    Category.total_unique_products = 0
    Category.all_products = set()

    p1 = Product("Телефон", "Смартфон", 50000.0, 10)
    p2 = Product("Ноутбук", "Игровой", 100000.0, 5)

    # Первая категория
    cat1 = Category("Электроника", "Техника", [p1, p2])
    assert cat1.counting_categories == 1
    assert cat1.total_unique_products == 2
