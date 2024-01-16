import unittest
from books.models import Book


class TestBookConstructor(unittest.TestCase):
    def test_invalid_name_raises_value_error(self):
        with self.assertRaises(ValueError):
            Book("1234567890123", "Homer", 800, "Epic")

    def test_invalid_author_raises_value_error(self):
        with self.assertRaises(ValueError):
            Book("Odyssey", "123 Homer", 800, "Epic")

    def test_name_with_special_characters(self):
        with self.assertRaises(ValueError):
            Book("Od*yssey", "Homer", 800, "Epic")

    def test_author_with_too_long_name(self):
        with self.assertRaises(ValueError):
            Book("Odyssey", "VeryLongAuthorNameIsHere", 800, "Epic")

    def test_author_with_special_characters(self):
        with self.assertRaises(ValueError):
            Book("Odyssey", "Homer!", 800, "Epic")


# Running the tests
if __name__ == "__main__":
    unittest.main()
