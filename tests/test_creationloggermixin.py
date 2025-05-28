import unittest

from src.creationloggermixin import CreationLoggerMixin


class TestReprMixin(unittest.TestCase):
    """Тесты для миксина CreationLoggerMixin"""

    def test_empty_object(self):
        """Тест пустого объекта"""

        class Empty(CreationLoggerMixin):
            pass

        obj = Empty()
        self.assertEqual(repr(obj), "Empty()")

    def test_public_attributes(self):
        """Тест с публичными атрибутами"""

        class TestClass(CreationLoggerMixin):
            def __init__(self, a, b):
                self.a = a
                self.b = b

        obj = TestClass(1, "test")
        self.assertEqual(repr(obj), "TestClass(a=1, b='test')")

    def test_private_attributes(self):
        """Тест с приватными атрибутами"""

        class TestClass(CreationLoggerMixin):
            def __init__(self, a):
                self.__private = a

        obj = TestClass("secret")
        self.assertEqual(repr(obj), "TestClass(private='secret')")

    def test_protected_attributes(self):
        """Тест с защищенными атрибутами"""

        class TestClass(CreationLoggerMixin):
            def __init__(self, a):
                self._protected = a

        obj = TestClass(42)
        self.assertEqual(repr(obj), "TestClass(protected=42)")

    def test_with_product_class(self):
        """Тест с классом Product"""

        class Product(CreationLoggerMixin):
            def __init__(self, name, price):
                self.name = name
                self.__price = price

        p = Product("Телефон", 50000)
        self.assertEqual(repr(p), "Product(name='Телефон', price=50000)")

    def test_multiple_inheritance(self):
        """Тест множественного наследования"""

        class Base:
            def __init__(self, x):
                self.x = x

        class TestClass(CreationLoggerMixin, Base):
            def __init__(self, x, y):
                super().__init__(x)
                self.y = y

        obj = TestClass(1, 2)
        self.assertEqual(repr(obj), "TestClass(x=1, y=2)")
