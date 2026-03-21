import pytest
from src.product import Product

# Проверяем, что переданные в инициализацию экземпляра (объекта) класса
# данные сохраняются в экземпляре (объекте) класса

@pytest.fixture
def product_milk():
    return Product('Молоко', 'Фермерское', 80.50, 25.00)


def test_init(product_milk):
    assert product_milk.name == 'Молоко'
    assert product_milk.description == 'Фермерское'
    assert product_milk.price == 80.50
    assert product_milk.quantity == 25.00
