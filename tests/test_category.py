import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class CategoryTests(unittest.TestCase):
    def test_search_by_category(self):
        lion = DigitalVideoDisc("The Lion King", "Animation")
        aladdin = DigitalVideoDisc("Aladdin", "Animation")
        star_wars = DigitalVideoDisc("Star Wars", "Science Fiction")
        items = [lion, aladdin, star_wars]

        self.assertEqual(
            search_by_category(items, "animation"),
            [lion, aladdin],
        )
        self.assertEqual(
            search_by_category(items, "ANIMATION"),
            [lion, aladdin],
        )
        self.assertEqual(search_by_category(items, "Drama"), [])
        self.assertEqual(search_by_category([], "Animation"), [])
        self.assertEqual(items, [lion, aladdin, star_wars])


if __name__ == "__main__":
    unittest.main()
