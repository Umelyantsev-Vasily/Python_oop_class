from src.create_class import Product


class Smartphone(Product):
    """Класс, представляющий смартфон в магазине."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: str,
        color: str,
    ):
        """Инициализирует новый смартфон."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        """Возвращает строковое представление смартфона."""
        return f"{self.name}, {self.model}, {self.color}, {self.price} руб. " f"Остаток: {self.quantity} шт."

    @property
    def price(self):
        return super().price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена должна быть положительной")
        super(Smartphone, self.__class__).price.fset(self, new_price)
