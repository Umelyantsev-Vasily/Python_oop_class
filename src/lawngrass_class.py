from src.create_class import Product


class LawnGrass(Product):
    """Класс, представляющий газонную траву в магазине. """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Инициализирует новую газонную траву. """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        """Возвращает строковое представление газонной травы. """
        return f"{self.name}, {self.country}, {self.color}, {self.price} руб. " f"Остаток: {self.quantity} шт."
