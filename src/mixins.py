class ReprMixin:
    """
    Миксин для вывода всех свойств объекта при инициализации.
    """

    def __init__(self, *args, **kwargs) -> None:
        # Вызываем __init__ родительских классов, если они есть
        super().__init__(*args, **kwargs)
        # Выводим строковое представление объекта, созданное __repr__
        print(f"Объект класса {self.__repr__()}")

    def __repr__(self):
        """
        Автоматически формирует __repr__ на основе всех атрибутов объекта.
        """
        # Получаем имя класса
        class_name = self.__class__.__name__
        # Получаем все атрибуты экземпляра, отфильтровывая методы
        attrs = ", ".join(
            f"{name_attr}={value_attr!r}"
            for name_attr, value_attr in self.__dict__.items()
        )
        return f"{class_name}({attrs})"


# if __name__ == '__main__':
#
#     class User(ReprMixin):
#
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age
#
#             # Обеспечивает вызов следующего класса в MRO
#             super().__init__()
#
#
#     # При создании объектов автоматически выводится их состояние
#     u = User("Alice", 30)
#     # Вывод: Объект класса User(name='Alice', age=30)
