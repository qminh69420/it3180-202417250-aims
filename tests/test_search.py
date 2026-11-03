import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTests(unittest.TestCase):
    def test_search_case_insensitive(self):
        lion = DigitalVideoDisc("The Lion King")
        aladdin = DigitalVideoDisc("Aladdin")
        items = [lion, aladdin]

        for keyword in ("lion", "LION", "Lion"):
            with self.subTest(keyword=keyword):
                self.assertEqual(
                    search_by_title(items, keyword),
                    [lion],
                )

        self.assertEqual(search_by_title(items, "missing"), [])
        self.assertEqual(search_by_title([], "lion"), [])
        self.assertEqual(search_by_title(items, ""), items)
        self.assertEqual(items, [lion, aladdin])


if __name__ == "__main__":
    unittest.main()
