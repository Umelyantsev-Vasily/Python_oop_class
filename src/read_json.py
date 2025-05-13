import json
from typing import List

from src.create_class import Category, Product


def load_categories_from_json(file_path: str) -> List[Category]:
    """
    Загружает категории и товары из JSON файла
    Возвращает список объектов Category
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Сброс счетчиков перед загрузкой
    Category.counting_categories = 0
    Category.total_unique_products = 0
    Category.all_products = set()

    categories = []
    for category_data in data:
        products = [
            Product(
                name=product["name"],
                description=product["description"],
                price=product["price"],
                quantity=product["quantity"],
            )
            for product in category_data["products"]
        ]

        categories.append(
            Category(name=category_data["name"], description=category_data["description"], products=products)
        )

    return categories
