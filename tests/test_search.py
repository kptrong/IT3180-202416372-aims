import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_title_case_insensitive(self):
        lion_king = DigitalVideoDisc("The Lion King")
        star_wars = DigitalVideoDisc("Star Wars")
        items = [lion_king, star_wars]

        self.assertEqual(
            search_by_title(items, "lion"),
            [lion_king],
        )
        self.assertEqual(
            search_by_title(items, "LION"),
            [lion_king],
        )


if __name__ == "__main__":
    unittest.main()