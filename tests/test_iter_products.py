import unittest
from src.iter_products import IterProducts
from src.product import Product


class TestIterProducts(unittest.TestCase):

    def test_iter_products_loop(self):
        product_1 = Product("Молоко_1", "Фермерское", 80.50, 25)
        product_2 = Product("Молоко_2", "Деревенское", 85.75, 10)
        product_3 = Product("Молоко_3", "Коровка", 105.50, 12)
        items = [product_1, product_2, product_3]
        iterator = IterProducts(items)
        result = [item for item in iterator]
        self.assertEqual(result, items)

    def test_iterator_next(self):
        product_4 = Product("Колбаса_1", "Докторская", 325.56, 51)
        product_5 = Product("Колбаса_2", "Любительская", 395.76, 11)
        product_6 = Product("Колбаса_3", "Ливерная", 298.70, 5)
        iterator = IterProducts([product_4, product_5, product_6])
        self.assertEqual(next(iterator), product_4)
        self.assertEqual(next(iterator), product_5)
        self.assertEqual(next(iterator), product_6)
        with self.assertRaises(StopIteration):
            next(iterator)
