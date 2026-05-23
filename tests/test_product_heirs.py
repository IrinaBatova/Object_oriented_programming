import unittest

import pytest

from src.product_heirs import Smartphone

smartphone1 = Smartphone(
    "Samsung Galaxy S23 Ultra",
    "256GB, Серый цвет, 200MP камера",
    180000.0,
    5,
    "Серый",
    "256GB",
    "S23 Ultra",
    95.5,
)
smartphone2 = Smartphone(
    "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
)

# Проверяем инициализацию с использованием конструктора экземпляра (объекта) класса Smartphone
def test_init_smartphone() -> None:
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.color == "Серый"
    assert smartphone1.efficiency == "256GB"
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 95.5

    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.color == 98.2
    assert smartphone2.efficiency == "15"
    assert smartphone2.model == 512
    assert smartphone2.memory == "Gray space"

if __name__ == "__main__":
    unittest.main()