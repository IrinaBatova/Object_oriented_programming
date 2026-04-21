from src.product import Product
from typing import Iterator


# 15.1 Магические методы. Дополнительное задание.
class IterProducts:
    """
    Класс IterProducts - вспомогательный класс (кастомный итератор для объектов класса Category), с помощью которого
    можно перебирать товары одной категории, например в цикле for
    """

    # Атрибуты (поля) класса. Определены на уровне класса, общие для всех экземпляров (объектов) класса.
    # Пока их нет.

    # Указываем типы атрибутов экземпляров класса — это часть аннотации типов, какие типы данных ожидаются для каждого
    # атрибута экземпляра класса
    obj_category_products: list[Product] # # Список товаров в категории
    current: int # Счетчик

    def __init__(self, obj_category_products: list) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        # Атрибуты (поля) экземпляра (объекта) класса. Определяются внутри метода __init__ через self. и уникальны для
        # каждого экземпляра (объекта) класса.
        self.obj_category_products = obj_category_products
        self.current = 0

    # def __repr__(self) -> str:
    #     return f"{self.__class__.__name__}('{self.obj_category_products}')"

    def __iter__(self) -> Iterator[Product]:
        """
        Магический метод, который делает объект итерируемым. Назначение - инициализация итерации и возврат итератора.
        :return: Объект - итератор (возвращает сам себя, так как объекты класса IterProducts являются итераторами)
        """
        return self

    def __next__(self) -> Product:
        """

        :return:
        """
        if self.current < len(self.obj_category_products):
            result = self.obj_category_products[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration
