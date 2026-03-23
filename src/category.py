from src.product import Product


class Category:
    """
    Класс Category
    """

    # Атрибуты (поля) класса. Определены на уровне класса, общие для всех экземпляров (объектов) класса.
    # Пока их нет.

    # Указываем типы атрибутов экземпляров класса — это часть аннотации типов,
    # какие типы данных ожидаются для каждого атрибута экземпляра класса
    name: str  # Название категории
    description: str  # Описание категории
    products: list[Product]  # Список товаров в категории
    category_count = 0  # Счетчик экземпляров (объектов) класса
    product_count = 0  # Счетчик количество продуктов в списке

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        # Атрибуты (поля) экземпляра (объекта) класса. Определяются внутри метода __init__ через self. и
        # уникальны для каждого экземпляра (объекта) класса.
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += (
            1  # Считаем сколько экземпляров (объектов) класса создано
        )
        Category.product_count = (
            len(products) if products else 0
        )  # Считаем количество продуктов в списке


# if __name__ == "__main__":
#     product1 = Product("Молоко_1", "Фермерское", 80.50, 25)
#     product_2 = Product("Молоко_2", "Деревенское", 85.75, 10)
#
#     category_1 = Category(
#         "Молочная продукция",
#         "Продукты в составе которых, основной ингредиент - молоко",
#         [product1, product_2],
#     )
#     print(category_1.name)
#     print(category_1.description)
#     print(len(category_1.products))
#     print(category_1.category_count)
#     print(category_1.product_count)
#
#     product_3 = Product("Колбаса_1", "Докторская", 325.56, 51)
#     product_4 = Product("Колбаса_2", "Любительская", 395.76, 11)
#     product_5 = Product("Колбаса_3", "Ливерная", 298.70, 5)
#
#     category_2 = Category(
#         "Мясная продукция",
#         "Продукты в составе которых, основной ингредиент - мясо",
#         [product_3, product_4, product_5],
#     )
#     print(category_2.name)
#     print(category_2.description)
#     print(len(category_2.products))
#     print(category_2.category_count)
#     print(category_2.product_count)
