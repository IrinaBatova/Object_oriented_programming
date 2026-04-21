import unittest

import pytest

from src.product import Product


# Проверяем, что переданные в инициализацию экземпляра (объекта) класса
# данные сохраняются в экземпляре (объекте) класса
@pytest.fixture
def product_milk():
    return Product("Молоко", "Фермерское", 80.50, 25)


# Проверяем инициализацию с использованием конструктора экземпляра (объекта) класса Product
def test_init(product_milk) -> None:
    assert product_milk.name == "Молоко"
    assert product_milk.description == "Фермерское"
    assert product_milk.price == 80.50
    assert product_milk.quantity == 25.00


# Проверяем инициализацию с использованием класс метода new_product экземпляра (объекта) класса Product
def test_new_product() -> None:
    new_product_1 = {
        "name": "Аленка",
        "description": "Молочный шоколад",
        "price": 125.00,
        "quantity": 46,
    }
    product_2 = Product.new_product(new_product_1)
    assert product_2.name == "Аленка"
    assert product_2.description == "Молочный шоколад"
    assert product_2.price == 125.00
    assert product_2.quantity == 46


# Проверяем работу геттера - возвращение значения приватного атрибута цены __price класса Product
def test_price_getter():
    product_1 = Product("Молоко", "Вкуснотеево", 95.50, 55)
    assert product_1.price == 95.50
    assert type(product_1.price) == float


# Проверяем работу сеттера для изменения приватного атрибута цены __price класса Product
def test_price_setter(product_milk):
    assert product_milk.price == 80.50
    product_milk.price = 95.50
    assert product_milk.price == 95.50


# Проверяем работу магического метода __repr__
def test_repr(product_milk):
    new_user = eval(repr(product_milk))
    assert product_milk.name == new_user.name
    assert product_milk.description == new_user.description


# Проверяем работу магического метода __str__
def test_str(product_milk):
    assert str(product_milk) == "Молоко, 80.5 руб. Остаток: 25 шт."


# Проверяем работу магического метода __add__
def test_add():
    product_1 = Product("Молоко", "Фермерское", 80.50, 25)
    product_2 = Product("Аленка", "Молочный шоколад", 125.00, 46)
    assert product_1 + product_2 == 7762.5


if __name__ == "__main__":
    unittest.main()
