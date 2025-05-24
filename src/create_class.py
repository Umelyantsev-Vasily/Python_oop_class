from typing import List, Set


class Product:
    """Класс, представляющий товар в магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализирует новый товар."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Возвращает цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новую цену товара."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Создает новый товар из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Складывает два продукта, возвращая их общую стоимость."""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return self.price * self.quantity + other.price * other.quantity

    def total_cost(self) -> float:
        """Возвращает общую стоимость товара (цена * количество)."""
        return self.price * self.quantity


class Category:
    """Класс, представляющий категорию товаров в магазине."""

    counting_categories: int = 0
    total_unique_products: int = 0
    all_products: Set[Product] = set()

    def __init__(self, name: str, description: str, products: List[Product] = None):
        """Инициализирует новую категорию."""
        self.name = name
        self.description = description
        self.__products = []

        Category.counting_categories += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        if product.quantity <= 0:
            print("Товар с нулевым количеством не может быть добавлен")
            return

        self.__products.append(product)
        Category.total_unique_products += 1
        Category.all_products.add(product)

    @property
    def products(self) -> str:
        """Возвращает список товаров в виде строк."""
        return "\n".join(str(product) for product in self.__products)

    @property
    def product_count(self) -> int:
        """Возвращает количество товаров в категории."""
        return len(self.__products)

    def __len__(self) -> int:
        """Возвращает общее количество товаров в категории (сумма quantity)."""
        return sum(product.quantity for product in self.__products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        return f"{self.name}, количество продуктов: {len(self)} шт."
