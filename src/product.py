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


# if __name__ == "__main__":
#     product_1 = Product("Молоко", "Фермерское", 80.50, 25)
#     print(product_1.name)
#     print(product_1.description)
#     print(product_1.price)
#     print(product_1.quantity)
