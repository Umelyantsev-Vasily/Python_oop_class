from src.create_class import Category, Product
from src.lawngrass_class import LawnGrass
from src.smartphone_class import Smartphone

if __name__ == "__main__":
    # Создание обычных продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создание категории
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Демонстрация базового функционала
    print("=== БАЗОВЫЙ ФУНКЦИОНАЛ ===")
    print("\nСписок продуктов после создания категории:")
    print(category1.products)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    print("\nСписок продуктов после добавления нового продукта:")
    print(category1.products)

    # Создание продукта через new_product
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S24",
            "description": "512GB, Черный, 250MP камера",
            "price": 220000.0,
            "quantity": 3,
        }
    )

    # Демонстрация работы с ценами
    print("\nРабота с ценами:")
    new_product.price = 800
    print("Новая цена (800):", new_product.price)

    try:
        new_product.price = -100
    except ValueError as e:
        print(f"Ошибка при установке цены -100: {e}")

    try:
        new_product.price = 0
    except ValueError as e:
        print(f"Ошибка при установке цены 0: {e}")

    # НОВАЯ ФУНКЦИОНАЛЬНОСТЬ
    print("\n=== НОВАЯ ФУНКЦИОНАЛЬНОСТЬ ===")

    # 1. Создание и работа с классами-наследниками
    smartphone = Smartphone("iPhone 15 Pro", "Флагман Apple", 150000, 10, "A17 Pro", "15 Pro", "1TB", "Titanium")

    lawn_grass = LawnGrass("Газонная трава Premium", "Мягкое покрытие", 2500, 100, "Италия", "14 дней", "Изумрудный")

    print("\nСпециализированные продукты:")
    print(smartphone)
    print(lawn_grass)

    # 2. Демонстрация сложения продуктов
    print("\nСложение продуктов:")
    try:
        total = smartphone + lawn_grass
        print(f"Общая стоимость: {total} руб.")
    except TypeError as e:
        print(f"Ошибка сложения разных классов: {e}")

    # 3. Добавление специализированных продуктов в категорию
    print("\nДобавление специализированных продуктов в категорию:")
    try:
        category1.add_product(smartphone)
        category1.add_product(lawn_grass)
        print("Продукты успешно добавлены!")
    except TypeError as e:
        print(f"Ошибка добавления: {e}")

    # 4. Статистика
    print("\nСтатистика:")
    print(f"Всего категорий: {Category.counting_categories}")
    print(f"Уникальных продуктов: {Category.total_unique_products}")
    print(f"Общее количество товаров в категории '{category1.name}': {len(category1)} шт.")
    print(f"Общая стоимость всех товаров: {sum(p.price * p.quantity for p in category1._Category__products)} руб.")

    # 5. Демонстрация защиты от добавления не-продуктов
    print("\nПопытка добавить не-продукт:")
    try:
        category1.add_product("Это не продукт")
    except TypeError as e:
        print(f"Ошибка: {e}")
