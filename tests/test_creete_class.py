from src.create_class import Product, Category


def test_category_initialization():
    p1 = Product("Телефон", "Смартфон", 50000.0, 10)
    p2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    category = Category("Электроника", "Техника", [p1, p2])

    assert category.name == "Электроника"
    assert len(category.products) == 2
    assert Category.counting_categories == 1
    assert Category.total_unique_products == 2


def test_products_counting():
    p1 = Product("Телефон", "Смартфон", 50000.0, 10)
    p2 = Product("Ноутбук", "Игровой", 100000.0, 5)

    # Первая категория
    cat1 = Category("Электроника", "Техника", [p1, p2])
    assert Category.counting_categories == 1
    assert Category.total_unique_products == 2

    # Вторая категория с одним новым товаром
    p3 = Product("Наушники", "Беспроводные", 5000.0, 20)
    cat2 = Category("Аксессуары", "Дополнительно", [p2, p3])

    assert Category.counting_categories == 2
    assert Category.total_unique_products == 3  # p1, p2, p3
