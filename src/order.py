from src.base_category_order import BaseCategoryOrder
from src.product import Product


class Order(BaseCategoryOrder):
    """
    Класс «Заказ»
    """

    # Указываем типы атрибутов экземпляров класса — это часть аннотации типов,
    # какие типы данных ожидаются для каждого атрибута экземпляра класса
    product_obj: Product  # Объект класса Product c информацией о товаре
    quantity_order: float  # Количество товара в заказе
    # final_cost: float # Итоговая стоимость товара

    def __init__(self, name, description, product_obj, quantity_order) -> None:

        # Вызов конструктора родительского класса BaseCategoryOrder
        super().__init__(name=name, description=description)

        # Атрибуты (поля) экземпляра (объекта) класса. Определяются внутри метода __init__ через self. и
        # уникальны для каждого экземпляра (объекта) класса.
        self.product_obj = product_obj
        self.quantity_order = quantity_order

    def __repr__(self) -> str:
        """
        Магический метод, предназначенный для создания «официального» строкового представления объекта,
        используется разработчиками для отладки, логирования, технического описания.
        :return: Строку (str)
        """

        return (
            f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.product_obj},"
            f" {self.quantity_order})"
        )

    def order_cost_calculation(self) -> float:
        final_cost = self.product_obj.price * self.quantity_order
        return final_cost

    def __str__(self) -> str:
        """
        Магический метод, определяющий читаемое описание объекта для пользователей.
        :return: Строку (str)
        """
        return (
            f"{self.name}, {self.description}, Наименование товара: {self.product_obj.name},"
            f" Цена товара: {self.product_obj.price}, Количество товара: {self.quantity_order} шт.,"
            f" Общая стоимость заказа: {self.order_cost_calculation()}"
        )


# if __name__ == "__main__":
#     product_1 = Product("Молоко_1", "Фермерское", 80.50, 25, "Белое")
#     product_2 = Product("Молоко_2", "Деревенское", 85.75, 10, "Розовое")
#
#     obj_order = Order("Заказ_1", "Срочный", product_1, 5)
#
#     print(obj_order)
