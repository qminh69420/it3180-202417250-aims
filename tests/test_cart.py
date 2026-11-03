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


if __name__ == "__main__":
    unittest.main()
