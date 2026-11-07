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



    def test_sort_by_title(self):
        cart = Cart()

        star_wars = DigitalVideoDisc("Star Wars", cost=10.0)
        aladdin = DigitalVideoDisc("Aladdin", cost=30.0)
        lion_king = DigitalVideoDisc("The Lion King", cost=20.0)

        for dvd in [star_wars, aladdin, lion_king]:
            cart.add_dvd(dvd)

        cart.sort_by_title()

        self.assertEqual(
            cart.items,
            [aladdin, star_wars, lion_king],
        )
        self.assertAlmostEqual(cart.total_cost(), 60.0)

    def test_sort_by_cost(self):
        cart = Cart()

        aladdin = DigitalVideoDisc("Aladdin", cost=30.0)
        lion_king = DigitalVideoDisc("The Lion King", cost=20.0)
        star_wars = DigitalVideoDisc("Star Wars", cost=10.0)

        for dvd in [aladdin, lion_king, star_wars]:
            cart.add_dvd(dvd)

        cart.sort_by_cost()

        self.assertEqual(
            cart.items,
            [star_wars, lion_king, aladdin],
        )
        self.assertAlmostEqual(cart.total_cost(), 60.0)
if __name__ == "__main__":
    unittest.main()