from src.product import Product
from src.order import Order


def test_init() -> None:
    product_1 = Product("Молоко_1", "Фермерское", 80.50, 25, "Белое")

    obj_order = Order("Заказ_1", "Срочный", product_1, 5)
    assert obj_order.name == "Заказ_1"
    assert obj_order.description == "Срочный"
    assert obj_order.order_cost_calculation() == 402.5
    assert (
        obj_order.__repr__()
        == "Order('Заказ_1', 'Срочный', Молоко_1, 80.5 руб. Остаток: 25 шт., 5)"
    )
    assert obj_order.__str__() == (
        "Заказ_1, Срочный, Наименование товара: Молоко_1, Цена товара: 80.5,"
        " Количество товара: 5 шт., Общая стоимость заказа: 402.5"
    )
