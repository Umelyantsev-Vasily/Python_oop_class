class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    counting_categories = 0  # подсчёт категорий
    total_unique_products = 0  # подсчёт УНИКАЛЬНЫХ товаров
    all_products = set()  # для хранения уникальных товаров

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # Обновляем счётчики
        Category.counting_categories += 1

        # Добавляем только новые уникальные товары
        new_products = set(self.products) - Category.all_products
        Category.all_products.update(new_products)
        Category.total_unique_products = len(Category.all_products)
