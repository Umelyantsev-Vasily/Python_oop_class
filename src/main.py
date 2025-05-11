from src.create_class import Category, Product

# def main():
#     # Загрузка данных
#     categories = load_categories_from_json(FAIL_PATH)
#
#     # Вывод результатов
#     print("=" * 50)
#     print("Загруженные категории:")
#     for category in categories:
#         print(f"\n{category}:")
#         for product in category.products:
#             print(f"  - {product}")
#
#     print("\n" + "=" * 50)
#     print(f"Всего категорий: {Category.counting_categories}")
#     print(f"Всего уникальных товаров: {Category.total_unique_products}")
#
#
# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Вывод информации о продуктах с заголовками
    print("=== Информация о продуктах ===")
    print(f"Название: {product1.name}")
    print(f"Описание: {product1.description}")
    print(f"Цена: {product1.price}")
    print(f"Количество: {product1.quantity}\n")

    print(f"Название: {product2.name}")
    print(f"Описание: {product2.description}")
    print(f"Цена: {product2.price}")
    print(f"Количество: {product2.quantity}\n")

    print(f"Название: {product3.name}")
    print(f"Описание: {product3.description}")
    print(f"Цена: {product3.price}")
    print(f"Количество: {product3.quantity}\n")

    # Создание и проверка категории смартфонов
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print("\n=== Проверка категории смартфонов ===")
    print(f"Название категории 'Смартфоны'? {category1.name == 'Смартфоны'}")
    print(f"Описание категории: {category1.description}")
    print(f"Количество продуктов в категории: {len(category1.products)}")
    print(f"Всего категорий (после создания этой): {category1.counting_categories}")
    print(f"Уникальных продуктов всего: {category1.total_unique_products}\n")

    # Создание и проверка категории телевизоров
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print("\n=== Проверка категории телевизоров ===")
    print(f"Название категории: {category2.name}")
    print(f"Описание категории: {category2.description}")
    print(f"Количество продуктов в категории: {len(category2.products)}")
    print("Список продуктов в категории:")
    for product in category2.products:
        print(f" - {product.name} ({product.price} руб.)")

    # Итоговые счетчики
    print("\n=== Итоговые счетчики ===")
    print(f"Всего категорий: {Category.counting_categories}")
    print(f"Всего уникальных продуктов: {Category.total_unique_products}")
