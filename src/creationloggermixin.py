class CreationLoggerMixin:
    """Миксин для логирования создания объектов и красивого repr"""

    def __init__(self, *args, **kwargs):
        """Логирует параметры создания объекта"""
        print(f"Создан объект класса {self.__class__.__name__} с параметрами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        # Вызываем следующий __init__ в цепочке наследования
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """Возвращает строковое представление объекта в формате:
        ClassName(attr1=value1, attr2=value2, ...)
        """
        params = []
        for name, value in self.__dict__.items():
            # Обработка приватных атрибутов (вида _ClassName__attr)
            if name.startswith(f"_{self.__class__.__name__}__"):
                name = name.split("__")[-1]
            # Обработка защищенных атрибутов (вида _attr)
            elif name.startswith("_"):
                name = name[1:]
            params.append(f"{name}={repr(value)}")
        return f"{self.__class__.__name__}({', '.join(params)})"
