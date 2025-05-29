from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для товаров"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @abstractmethod
    def new_product(cls, product_data: dict) -> "BaseProduct":
        pass
