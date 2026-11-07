import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()

        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"DVD {i + 1}")
            self.assertTrue(cart.add_dvd(dvd))

        extra_dvd = DigitalVideoDisc("DVD 21")

        self.assertFalse(cart.add_dvd(extra_dvd))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD A", cost=10.0))
        cart.add_dvd(DigitalVideoDisc("DVD B", cost=20.0))

        self.assertAlmostEqual(cart.total_cost(), 30.0)

    def test_total_cost_with_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD A", cost=100.0))

        self.assertAlmostEqual(
            cart.total_cost_with_discount(20),
            80.0,
        )

    def test_discount_percent_out_of_range(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD A", cost=100.0))

        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)
if __name__ == "__main__":
    unittest.main()