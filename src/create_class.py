from typing import List, Set


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Класс-метод для создания продукта из словаря"""
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
        self.__products = []  # Приватный атрибут

        Category.counting_categories += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        self.__products.append(product)

        if product not in Category.all_products:
            Category.all_products.add(product)
            Category.total_unique_products = len(Category.all_products)

    @property
    def products(self) -> List[Product]:
        """Геттер для получения списка товаров"""
        return self.__products

    def __len__(self) -> int:
        """Возвращает количество товаров в категории"""
        return len(self.__products)
