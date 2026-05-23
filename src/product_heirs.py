from src.product import Product

# 16.1 Наследование. Задание_1.


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
        self.color = color # Цвет

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

if __name__ == '__main__':
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                             180000.0, 5, "Серый",
                             "256GB", "S23 Ultra", 95.5)
    print(smartphone1)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                       "Россия", "7 дней", "Зеленый")
    print(grass1)