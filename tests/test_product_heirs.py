import unittest

import pytest

from src.product_heirs import LawnGrass, Smartphone

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

grass1 = LawnGrass(
    "Газонная трава",
    "Элитная трава для газона",
    500.0,
    20,
    "Россия",
    "7 дней",
    "Зеленый",
)
grass2 = LawnGrass(
    "Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый"
)


# Проверяем инициализацию с использованием конструктора экземпляра (объекта) класса "Smartphone"
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


# Проверяем работу магического метода __add__ класса "Smartphone"


def test_add_smartphone() -> None:
    assert smartphone1 + smartphone2 == 2580000.00


def test_add_smartphone_raises() -> None:
    # Проверка типа и соответствия сообщения регулярному выражению
    with pytest.raises(
        TypeError, match="Складывать можно только объекты класса Smartphone."
    ):
        smartphone1 + grass1


# Проверяем инициализацию с использованием конструктора экземпляра (объекта) класса "LawnGrass"
def test_init_lawngrass() -> None:
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.color == "Россия"
    assert grass1.country == "7 дней"
    assert grass1.germination_period == "Зеленый"


# Проверяем работу магического метода __add__ класса "LawnGrass"


def test_add_lawngrass() -> None:
    assert grass1 + grass2 == 16750.0


def test_add_lawngrass_raises() -> None:
    # Проверка типа и соответствия сообщения регулярному выражению
    with pytest.raises(
        TypeError, match="Складывать можно только объекты одного класса."
    ):
        grass1 + smartphone1


if __name__ == "__main__":
    unittest.main()
