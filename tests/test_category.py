import pytest
from src.category import Category

# Проверяем, что переданные в инициализацию экземпляра (объекта) класса
# данные сохраняются в экземпляре (объекте) класса

@pytest.fixture
def category_milk():
    return Category('Молочная продукция', 'Продукты в составе которых, основной ингредиент - молоко', ['Молоко 1', 'Молоко 2', 'Молоко 3'])


def test_init(category_milk):
    assert category_milk.name == 'Молочная продукция'
    assert category_milk.description == 'Продукты в составе которых, основной ингредиент - молоко'
    assert category_milk.products == ['Молоко 1', 'Молоко 2', 'Молоко 3']
