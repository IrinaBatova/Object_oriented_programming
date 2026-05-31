from abc import ABC, abstractmethod


class BaseProduct(ABC):

    # Атрибуты (поля) класса. Определены на уровне класса, общие для всех экземпляров (объектов) класса.
    # Пока их нет.

    # Указываем типы атрибутов экземпляров класса — это часть аннотации типов,
    # какие типы данных ожидаются для каждого атрибута экземпляра класса-наследника
    name: str  # Название продукта
    description: str  # Описание продукта

    def __init__(self, name, description) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        # Атрибуты (поля) экземпляра (объекта) класса. Определяются внутри метода __init__ через self. и
        # уникальны для каждого экземпляра (объекта) класса.
        # super().__init__()  # Обеспечивает вызов следующего класса в MRO
        self.name = name
        self.description = description
        super().__init__()  # Обеспечивает вызов следующего класса в MRO

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        pass


# if __name__ == "__main__":
#
#     print(BaseProduct)

    # abc = BaseProduct()
