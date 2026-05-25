from src.iter_products import IterProducts
from src.product import Product


class Category:
    """
    Класс Category
    """

    # Атрибуты (поля) класса. Определены на уровне класса, общие для всех экземпляров (объектов) класса.
    category_count = 0  # Счетчик экземпляров (объектов) класса
    product_count = 0  # Счетчик количества продуктов в списке

    # Указываем типы атрибутов экземпляров класса — это часть аннотации типов, какие типы данных ожидаются для каждого
    # атрибута экземпляра класса
    name: str  # Название категории
    description: str  # Описание категории
    products: list[Product]  # Список товаров в категории

    def __init__(self, name, description, products) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        # Атрибуты (поля) экземпляра (объекта) класса. Определяются внутри метода __init__ через self. и уникальны для
        # каждого экземпляра (объекта) класса.
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут

        # Считаем сколько экземпляров (объектов) класса создано
        Category.category_count += 1

        # Считаем количество продуктов в списке при инициализации экземпляра (объекта) класса
        Category.product_count = len(products) if products else 0

    # 14.2 Режимы доступа. Задание_1. # 16.1 Наследование. Задание_3

    def add_product(self, product_object: Product) -> None:
        """
        Метод добавляет экземпляр (объект) класса Product в приватный атрибут __products класса Category
        :param product_object: экземпляр (объект) класса Product
        :return: метод ничего не возвращает
        """
        if isinstance(product_object, Product):
            self.__products.append(product_object)
        else:
            raise TypeError(
                "Добавлять можно только объекты класса Product или его подклассов."
            )

        # Увеличиваем счетчик продуктов на единицу.
        Category.product_count += 1

    # Защитить метод так, чтобы, кроме смартфонов, травы газонной или других продуктов, в список нельзя было добавлять
    # ничего другого. Доработайте метод, который добавляет продукт в категорию, таким образом, чтобы не было
    # возможности добавить вместо продукта или его наследников любой другой объект.

    # 14.2 Режимы доступа. Задание_2.

    @property
    def products(self) -> str:
        """
        Геттер - выводит список товаров в виде строк в формате: "Название продукта, X руб. Остаток: X шт.\n"
        :return: Строку (str)
        """
        product_strings = []

        # Оптимизируем работу геттера так, чтобы он использовал новый метод __str__ класса Product
        for product_obj in self.__products:
            product_str = str(product_obj)
            product_strings.append(product_str)
        return "\n".join(product_strings)

        # for product_obj in self.__products:
        #     product_str = (
        #         f"{product_obj.name}, {product_obj.price} руб. Остаток: {product_obj.quantity} шт."
        #     )
        #     product_strings.append(product_str)
        # return "\n".join(product_strings)

    # def set_products(self, products: list):
    #     """
    #     Сеттер - метод, устанавливающий новое значение приватного атрибута __products
    #     """
    #     self.__products = products

    def len_products(self) -> int:
        """
        Метод считает количество продуктов
        :return: целое число
        """
        return len(self.__products)

    # 15.1 Магические методы. Задание_1.

    # def __repr__(self) -> str:
    #     """
    #     Магический метод, предназначенный для создания «официального» строкового представления объекта,
    #     используется разработчиками для отладки, логирования, технического описания.
    #     :return: Строку (str)
    #     """
    #     return f"{self.__class__.__name__}('{self.obj_category}')"

    def __str__(self) -> str:
        """
        Магический метод, определяющий читаемое описание объекта для пользователей.
        :return: Строку (str)
        """
        quantity_products = sum(product_obj.quantity for product_obj in self.__products)
        return f"{self.name}, общее количество продуктов: {quantity_products} шт."

    # def __str__(self):
    #     quantity_products = 0
    #     for el in self.__products:
    #         quantity_products += el.quantity
    #     return f"{self.name}, общее количество продуктов: {quantity_products} шт."

    # 15.1 Магические методы. Дополнительное задание.
    def __iter__(self) -> IterProducts:
        """
        Магический метод, который делает объект итерируемым. Назначение - инициализация итерации и возврат итератора.
        :return: Объект - итератор класса IterProducts
        """
        return IterProducts(self.__products)


# if __name__ == "__main__":
#     product_1 = Product("Молоко_1", "Фермерское", 80.50, 25)
#     product_2 = Product("Молоко_2", "Деревенское", 85.75, 10)
#     category_1 = Category(
#         "Молочная продукция",
#         "Продукты в составе которых, основной ингредиент - молоко",
#         [product_1, product_2])
#
#     print(iter(category_1))
#
#     items = []
#
#     for el in category_1:
#         items.append(el)
#
#     print(items)
#
#     print(category_1)
#
#
#     print(category_1.name)
#     print(category_1.description)
#     print(category_1.category_count)
#     print(category_1.product_count)
#
#     print(category_1.products)
#     print(category_1.len_products())
#     category_1.add_product(product_2)
#     print(category_1.products)
#     print(category_1.len_products())
#     print(category_1)
#
#     print(dir(category_1))
#
#     product_3 = Product("Колбаса_1", "Докторская", 325.56, 51)
#     product_4 = Product("Колбаса_2", "Любительская", 395.76, 11)
#     product_5 = Product("Колбаса_3", "Ливерная", 298.70, 5)
#     product_6 = Product("Колбаса_4", "Останкинская", 364.70, 234)
#
#     category_2 = Category(
#         "Мясная продукция",
#         "Продукты в составе которых, основной ингредиент - мясо",
#         [product_3, product_4, product_5],
#     )
#
#     category_2.add_product(product_6)
#
#     for el in category_2:
#         print(el)
#
#     print(category_2.name)
#     print(category_2.description)
#     print(category_2.category_count)
#     print(category_2.product_count)
#     print(category_2.len_products())
#     print(category_2.products)
