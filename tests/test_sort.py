import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class SortTests(unittest.TestCase):
    def test_sort_by_title(self):
        cart = Cart()
        cart.items = [
            DigitalVideoDisc("Star Wars", cost=24.95),
            DigitalVideoDisc("aladdin", cost=18.99),
            DigitalVideoDisc("The Lion King", cost=19.95),
        ]

        cart.sort_by_title()

        self.assertEqual(
            [dvd.title for dvd in cart.items],
            ["aladdin", "Star Wars", "The Lion King"],
        )
        self.assertEqual(cart.total_cost(), 63.89)

    def test_sort_by_cost(self):
        cart = Cart()
        cart.items = [
            DigitalVideoDisc("B", cost=20),
            DigitalVideoDisc("C", cost=10),
            DigitalVideoDisc("A", cost=10),
        ]

        cart.sort_by_cost()

        self.assertEqual(
            [dvd.title for dvd in cart.items],
            ["A", "C", "B"],
        )
        self.assertEqual(cart.total_cost(), 40)


if __name__ == "__main__":
    unittest.main()
