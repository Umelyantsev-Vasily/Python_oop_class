from typing import List, Set


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )


class Category:
    counting_categories: int = 0
    total_unique_products: int = 0
    all_products: Set[Product] = set()

    def __init__(self, name: str, description: str, products: List[Product] = None):
        self.name = name
        self.description = description
        self.__products = []

        Category.counting_categories += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        if product.quantity <= 0:
            print("Товар с нулевым количеством не может быть добавлен")
            return

        self.__products.append(product)
        Category.total_unique_products += 1  # Увеличиваем при каждом добавлении
        Category.all_products.add(product)  # Добавляем в множество уникальных

    @property
    def products(self) -> str:
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    @property
    def product_count(self) -> int:
        return len(self.__products)

    def __len__(self) -> int:
        return sum(product.quantity for product in self.__products)
