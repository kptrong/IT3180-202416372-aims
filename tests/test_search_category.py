import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchCategory(unittest.TestCase):
    def test_search_by_category(self):
        lion_king = DigitalVideoDisc(
            "The Lion King", category="Animation"
        )
        star_wars = DigitalVideoDisc(
            "Star Wars", category="Science Fiction"
        )
        aladdin = DigitalVideoDisc(
            "Aladdin", category="Animation"
        )

        items = [lion_king, star_wars, aladdin]

        result = search_by_category(items, "Animation")

        self.assertEqual(result, [lion_king, aladdin])


if __name__ == "__main__":
    unittest.main()