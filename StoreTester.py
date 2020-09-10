# Zaki Ahmed
# 04 Apr 2020
# Assignment 2

# CS 162 : Sp 2020
# Description: A store tester that runs with products, customers, and store checkouts

import unittest
import Store

class TestStore(unittest.TestCase):
    """
    Summary: Test our Store.py file with 5 unit tests, using 3 different assert functions
    Parameters:
    Returns:
    """

# Using 1 type of unit test
    def test_1(self):
        p1 = Store.Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        product_id = p1.get_product_id()
        self.assertEqual(product_id, "889")

    def test_2(self):
        p1 = Store.Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        title = p1.get_title()
        self.assertEqual(title, "Rodent of unusual size")

    def test_3(self):
        p1 = Store.Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        description = p1.get_description()
        self.assertEqual(description, "when a rodent of the usual size just won't do")

# Using 2 other types of unit tests
    def test_4(self):
        c1 = Store.Customer("Yinsheng", "QWF", False)
        membership = c1.is_premium_member()
        self.assertIs(membership, False)

    def test_5(self):
        c1 = Store.Customer("Yinsheng", "QWF", False)
        name = c1.get_name()
        self.assertIn(name, "Yinsheng")


if __name__ == '__main__':
    unittest.main()