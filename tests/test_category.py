import unittest
from unittest import mock

import pytest

from src.category import Category
from src.product import Product

# Проверяем, что переданные в инициализацию экземпляра (объекта) класса
# данные сохраняются в экземпляре (объекте) класса


@pytest.fixture
def category_milk() -> Category:

    # Создаем список экземпляров (объектов) нужного класса
    product_1 = Product("Молоко_1", "Фермерское", 80.50, 25)
    product_2 = Product("Молоко_2", "Деревенское", 85.75, 10)

    return Category(
        "Молочная продукция",
        "Продукты в составе которых, основной ингредиент - молоко",
        [product_1, product_2],
    )


def test_init(category_milk: Category) -> None:
    assert category_milk.name == "Молочная продукция"
    assert (
        category_milk.description
        == "Продукты в составе которых, основной ингредиент - молоко"
    )
    # assert isinstance(category_milk.products, list)  # Проверка, что это список
    assert category_milk.len_products() == 2  # Проверка длины списка


# Проверяем количество, созданных экземпляров (объектов) класса Category
def test_category_count() -> None:
    with mock.patch.object(Category, "category_count", new=5):
        assert Category.category_count == 5


# Проверяем количество продуктов в категории в экземпляре класса Category
def test_product_count(category_milk: Category) -> None:
    assert category_milk.product_count == 2


# Проверяем, что метод add_product класса Category добавляет один продукт в категорию
def test_add_product(category_milk: Category) -> None:
    product_3 = Product("Молоко_3", "Вкуснотеево", 59.75, 16)
    category_milk.add_product(product_3)
    assert category_milk.product_count == 3


# Проверяем, что Геттер products - выводит список товаров в виде строк
def test_products():
    product_3 = Product("Колбаса_1", "Докторская", 325.56, 51)
    product_4 = Product("Колбаса_2", "Любительская", 395.76, 11)
    product_5 = Product("Колбаса_3", "Ливерная", 298.70, 5)
    product_6 = Product("Колбаса_4", "Останкинская", 364.70, 234)

    category_2 = Category(
        "Мясная продукция",
        "Продукты в составе которых, основной ингредиент - мясо",
        [product_3, product_4, product_5, product_6],
    )

    assert category_2.products == (
        "Колбаса_1, 325.56 руб. Остаток: 51 шт.\n"
        "Колбаса_2, 395.76 руб. Остаток: 11 шт.\n"
        "Колбаса_3, 298.7 руб. Остаток: 5 шт.\n"
        "Колбаса_4, 364.7 руб. Остаток: 234 шт."
    )


if __name__ == "__main__":
    unittest.main()
