import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()

        for index in range(20):
            dvd = DigitalVideoDisc(f"DVD {index + 1}")
            self.assertTrue(cart.add_digital_video_disc(dvd))

        self.assertEqual(len(cart.items), 20)

        accepted = cart.add_digital_video_disc(
            DigitalVideoDisc("DVD 21")
        )

        self.assertFalse(accepted)
        self.assertEqual(len(cart.items), 20)

    def test_total_cost(self):
        cart = Cart()
        self.assertEqual(cart.total_cost(), 0)

        cart.add_digital_video_disc(
            DigitalVideoDisc("The Lion King", cost=19.95)
        )
        cart.add_digital_video_disc(
            DigitalVideoDisc("Star Wars", cost=24.95)
        )
        cart.add_digital_video_disc(
            DigitalVideoDisc("Aladdin", cost=18.99)
        )

        self.assertEqual(cart.total_cost(), 63.89)

    def test_discount(self):
        cart = Cart()
        cart.add_digital_video_disc(
            DigitalVideoDisc("Test DVD", cost=100)
        )

        self.assertEqual(cart.total_cost_with_discount(20), 80)
        self.assertEqual(cart.total_cost_with_discount(0), 100)
        self.assertEqual(cart.total_cost_with_discount(100), 0)

    def test_invalid_discount(self):
        cart = Cart()

        for percent in (-1, 150):
            with self.subTest(percent=percent):
                with self.assertRaises(ValueError):
                    cart.total_cost_with_discount(percent)
if __name__ == "__main__":
    unittest.main()
