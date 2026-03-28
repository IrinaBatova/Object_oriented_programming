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


    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        # Атрибуты (поля) экземпляра (объекта) класса. Определяются внутри метода __init__ через self. и уникальны для
        # каждого экземпляра (объекта) класса.
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут

        # Считаем сколько экземпляров (объектов) класса создано
        Category.category_count += 1

        # Считаем количество продуктов в списке при инициализации экземпляра (объекта) класса
        Category.product_count = (len(products) if products else 0)


# 14.2 Режимы доступа. Задание_1.

    def add_product(self, product: Product) -> None:
        """
        Метод добавляет экземпляр (объект) класса Product в приватный атрибут __products класса Category
        :param product: экземпляр (объект) класса Product
        :return: метод ничего не возвращает
        """
        self.__products.append(product)

        # Увеличиваем счетчик продуктов на единицу.
        Category.product_count += 1


# 14.2 Режимы доступа. Задание_2.

    @property
    def products(self):
        """
        Геттер - выводит список товаров в виде строк в формате: "Название продукта, X руб. Остаток: X шт.\n"
        :return:
        """
        product_strings = []

        for product in self.__products:
            product_str = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            product_strings.append(product_str)
        return "\n".join(product_strings)


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


# if __name__ == "__main__":
#     product_1 = Product("Молоко_1", "Фермерское", 80.50, 25)
#     product_2 = Product("Молоко_2", "Деревенское", 85.75, 10)
#
#     category_1 = Category(
#         "Молочная продукция",
#         "Продукты в составе которых, основной ингредиент - молоко",
#         [product_1])
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
#
#     pprint(dir(category_1))
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
#     category_2.add_product(product_6)
#     print(category_2.name)
#     print(category_2.description)
#     print(category_2.category_count)
#     print(category_2.product_count)
#     print(category_2.len_products())
#     print(category_2.products)
