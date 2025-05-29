from typing import Dict, List, Set

from src.base_product import BaseProduct
from src.creationloggermixin import CreationLoggerMixin


class Product(CreationLoggerMixin, BaseProduct):
    """Класс товара с логированием создания объектов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация товара с логированием"""
        super().__init__(name=name, description=description, price=price, quantity=quantity)

        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Возвращает цену товара"""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Устанавливает новую цену товара"""
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self.__price = value

    @classmethod
    def new_product(cls, product_data: Dict[str, object]) -> "Product":
        """Создает новый товар из словаря"""
        quantity = int(product_data["quantity"])
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        return cls(
            name=str(product_data["name"]),
            description=str(product_data["description"]),
            price=float(product_data["price"]),
            quantity=quantity,
        )

    def __str__(self) -> str:
        """Строковое представление товара"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def total_cost(self) -> float:
        """Возвращает общую стоимость товара (цена * количество)"""
        return self.price * self.quantity

    def __add__(self, other: "Product") -> float:
        """Сложение товаров по общей стоимости"""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product или его наследников")
        if type(self) != type(other):
            raise TypeError("Можно складывать только объекты класса Product или его наследников")
        return self.total_cost() + other.total_cost()


class Smartphone(Product):
    """Класс для представления смартфона"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Smartphone") -> float:
        return super().__add__(other)


class LawnGrass(Product):
    """Класс для представления газонной травы"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "LawnGrass") -> float:
        return super().__add__(other)


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
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        if product.quantity <= 0:
            print("Товар с нулевым количеством не может быть добавлен")
            return

        if product not in self.__products:
            self.__products.append(product)
            Category.total_unique_products += 1
            Category.all_products.add(product)

    @property
    def products(self) -> str:
        """Возвращает список товаров в виде строк."""
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> List[Product]:
        """Возвращает список товаров (для внутреннего использования)."""
        return self.__products

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

    def average_price(self) -> float:
        """
        Рассчитывает среднюю цену товаров в категории.
        Возвращает 0, если в категории нет товаров.
        """
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0.0

