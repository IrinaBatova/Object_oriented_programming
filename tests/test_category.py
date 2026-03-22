import unittest
from unittest import mock

import pytest

from src.category import Category

# Проверяем, что переданные в инициализацию экземпляра (объекта) класса
# данные сохраняются в экземпляре (объекте) класса


@pytest.fixture
def category_milk() -> Category:
    return Category(
        "Молочная продукция",
        "Продукты в составе которых, основной ингредиент - молоко",
        ["Молоко 1", "Молоко 2", "Молоко 3"],
    )


def test_init(category_milk: Category) -> None:
    assert category_milk.name == "Молочная продукция"
    assert (
        category_milk.description
        == "Продукты в составе которых, основной ингредиент - молоко"
    )
    assert category_milk.products == ["Молоко 1", "Молоко 2", "Молоко 3"]


# Проверяем количество категорий
def test_category_count() -> None:
    with mock.patch.object(Category, "category_count", new=5):
        assert Category.category_count == 5


# Проверяем количество продуктов в категории
def test_product_count(category_milk: Category) -> None:
    assert category_milk.product_count == 3


if __name__ == "__main__":
    unittest.main()
