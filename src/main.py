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

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print("Список продуктов после создания категории:")
    print(category1.products)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    print("\nСписок продуктов после добавления нового продукта:")
    print(category1.products)

    print("\nКоличество продуктов в категории:", category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )

    print("\nИнформация о новом продукте:")
    print("Название:", new_product.name)
    print("Описание:", new_product.description)
    print("Цена:", new_product.price)
    print("Количество:", new_product.quantity)

    print("\nИзменение цены продукта:")
    new_product.price = 800
    print("Новая цена (800):", new_product.price)

    print("\nПопытка установки недопустимых цен:")
    new_product.price = -100
    print("Цена после попытки установки -100:", new_product.price)
    new_product.price = 0
    print("Цена после попытки установки 0:", new_product.price)
