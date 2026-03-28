from typing import TypeVar, Type

P = TypeVar("P", bound="Product")

class Product:
    """
    Класс Product
    """

    # Атрибуты (поля) класса. Определены на уровне класса, общие для всех экземпляров (объектов) класса.
    # Пока их нет.

    # Указываем типы атрибутов экземпляров класса — это часть аннотации типов,
    # какие типы данных ожидаются для каждого атрибута экземпляра класса
    name: str  # Название продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: float  # Количество продукта в наличии

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        # Атрибуты (поля) экземпляра (объекта) класса. Определяются внутри метода __init__ через self. и
        # уникальны для каждого экземпляра (объекта) класса.
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

# 14.2 Режимы доступа. Задание_3.

    @classmethod
    def new_product(cls:Type[P], product_dict: dict) -> P:
        """
        Класс метод, который принимает на вход данные на продукт в виде словаря и возвращает созданный объект класса Product
        :param product_dict: данные на продукт в виде словаря для создания объекта класса Product
        :return: возвращает экземпляр класса Product на основе данных словаря
        """
        name = product_dict['name']
        description = product_dict['description']
        price = product_dict['price']
        quantity = product_dict['quantity']

        return cls(name, description, price, quantity)


if __name__ == "__main__":
#     product_1 = Product("Молоко", "Фермерское", 80.50, 25)
#     print(product_1.name)
#     print(product_1.description)
#     print(product_1.price)
#     print(product_1.quantity)

    new_product_1 = {'name': 'Аленка', 'description': 'Молочный шоколад', 'price': 125.00, 'quantity': 46}
    product_2 = Product.new_product(new_product_1)
    print(product_2)
