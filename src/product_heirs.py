from src.product import Product

# 16.1 Наследование. Задание_1. Создаем класс "Smartphone"


class Smartphone(Product):
    """
    Smartphone ("Смартфон") класс наследник класса Product
    """

    # Атрибуты (поля) класса. Определены на уровне класса, общие для всех экземпляров (объектов) класса.
    # Пока их нет.

    # Указываем типы атрибутов экземпляров класса — это часть аннотации типов,
    # какие типы данных ожидаются для каждого атрибута экземпляра класса
    efficiency: str  # Производительность
    model: str  # Модель
    memory: float  # Объем встроенной памяти

    # Переопределяем магический метод __init__ базового класса
    def __init__(
        self, name, description, price, quantity, color, efficiency, model, memory
    ):

        # Вызываем метод __init__ базового класса
        super().__init__(name, description, price, quantity)

        # Дополнительный код новые атрибуты (поля) экземпляра (объекта) класса Smartphone
        self.efficiency = efficiency  # Производительность
        self.model = model  # Модель
        self.memory = memory  # Объем встроенной памяти
        self.color = color  # Цвет

    # 16.1 Наследование. Задание_2. Переопределяем метод __add__ для класса Smartphone

    def __add__(self, other_obj: "Product") -> float:
        """
        Метод реализует возможность складывать два объекта(экземпляра) класса Smartphone, текущий и
        переданный в качестве аргумента other_obj
        :param other_obj: Другой объект класса Smartphone
        :return: метод возвращает сумму произведений цены на количество у двух объектов класса Smartphone
        """

        if type(other_obj) is Smartphone:
            sum_obj = super().__add__(other_obj)
            return sum_obj
        else:
            raise TypeError("Складывать можно только объекты класса Smartphone.")

        # if isinstance(other_obj, Smartphone):
        #     sum_obj = super().__add__(other_obj)
        #     return sum_obj
        # else:
        #     raise TypeError('Складывать можно только объекты класса Smartphone и дочерние от них.')

    # Доработайте функциональность сложения таким образом, чтобы можно было складывать товары только из одинаковых
    # классов продуктов. То есть новая функциональность не должна давать возможность сложить смартфон и траву газонную,
    # вместо этого должна быть выдана ошибка TypeError.


# 16.1 Наследование. Задание_1. Создаем класс "LawnGrass"


class LawnGrass(Product):
    """
    LawnGrass ("Трава газонная") класс наследник класса Product
    """

    # Переопределяем магический метод __init__ базового класса
    def __init__(
        self, name, description, price, quantity, color, country, germination_period
    ):
        # Вызываем метод __init__ базового класса
        super().__init__(name, description, price, quantity)

        # Дополнительный код новые атрибуты (поля) экземпляра (объекта) класса LawnGrass
        self.country = country  # Страна-производитель
        self.germination_period = germination_period  # Срок прорастания
        self.color = color  # Цвет

    # 16.1 Наследование. Задание_2. Переопределяем метод __add__ для класса LawnGrass

    def __add__(self, other_obj: "Product") -> float:
        """
        Метод реализует возможность складывать два объекта(экземпляра) класса LawnGrass, текущий и
        переданный в качестве аргумента other_obj
        :param other_obj: Другой объект класса LawnGrass
        :return: метод возвращает сумму произведений цены на количество у двух объектов класса LawnGrass
        """

        if type(self) is type(other_obj):
            sum_obj = super().__add__(other_obj)
            return sum_obj
        else:
            raise TypeError("Складывать можно только объекты одного класса.")

        # if type(other_obj) == LawnGrass:
        #     sum_obj = super().__add__(other_obj)
        #     return sum_obj
        # else:
        #     raise TypeError('Складывать можно только объекты класса LawnGrass.')
        #
        #
        # if isinstance(other_obj, LawnGrass):
        #     sum_obj = super().__add__(other_obj)
        #     return sum_obj
        # else:
        #     raise TypeError('Складывать можно только объекты класса LawnGrass и дочерние от него.')


# if __name__ == '__main__':
#     smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
#                              180000.0, 5, "Серый",
#                              "256GB", "S23 Ultra", 95.5)
#     print(smartphone1)
#
#     smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
#
#     grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
#                        "Россия", "7 дней", "Зеленый")
#     print(grass1)
#
#     grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
#
#     print(smartphone1 + smartphone2)
#     # print(smartphone1 + grass1)
#
#     print(grass1 + grass2)
#     # print(grass1 + smartphone1)
