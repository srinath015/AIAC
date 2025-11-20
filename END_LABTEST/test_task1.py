import unittest

from TASK1 import find_highest_rated_product


class TestFindHighestRatedProduct(unittest.TestCase):
    """
    Unit tests for the find_highest_rated_product function.
    This test suite verifies the following behaviors:
    - Correctly identifies the highest-rated product from multiple entries.
    - Handles a single product rating.
    - Correctly manages ties in ratings, returning any product with the highest rating.
    - Raises ValueError when given an empty dictionary.
    - Raises TypeError when input is not a dictionary.
    - Handles negative ratings and identifies the highest (least negative) value.
    - Handles zero ratings and manages ties.
    - Supports non-string keys in the ratings dictionary.
    - Raises TypeError when any rating value is non-numeric.
    - Correctly processes a large number of products and identifies the highest-rated one.
    """
    def test_multiple_products(self):
        ratings = {
            "Laptop": 4.7,
            "Mouse": 4.2,
            "Keyboard": 4.9,
            "Monitor": 4.5,
        }
        self.assertEqual(find_highest_rated_product(ratings), ("Keyboard", 4.9))

    def test_single_product(self):
        ratings = {"Headphones": 4.6}
        self.assertEqual(find_highest_rated_product(ratings), ("Headphones", 4.6))

    def test_tie_ratings(self):
        ratings = {"Phone": 4.8, "Tablet": 4.8, "Charger": 4.3}
        product, rating = find_highest_rated_product(ratings)
        self.assertEqual(rating, 4.8)
        self.assertIn(product, ("Phone", "Tablet"))

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            find_highest_rated_product({})

    def test_non_dict_raises(self):
        with self.assertRaises(TypeError):
            find_highest_rated_product([("a", 1)])

    def test_negative_ratings(self):
        ratings = {"A": -1.0, "B": -2.0, "C": -0.5}
        self.assertEqual(find_highest_rated_product(ratings), ("C", -0.5))

    def test_zero_ratings(self):
        ratings = {"A": 0.0, "B": 0.0}
        product, rating = find_highest_rated_product(ratings)
        self.assertEqual(rating, 0.0)
        self.assertIn(product, ("A", "B"))

    def test_non_string_keys(self):
        ratings = {1: 4.5, 2: 4.8}
        self.assertEqual(find_highest_rated_product(ratings), (2, 4.8))

    def test_non_numeric_values_raises(self):
        ratings = {"A": "high", "B": 4.5}
        with self.assertRaises(TypeError):
            find_highest_rated_product(ratings)

    def test_large_number_of_products(self):
        ratings = {f"Product{i}": i * 0.1 for i in range(100)}
        self.assertEqual(find_highest_rated_product(ratings), ("Product99", 9.9))


if __name__ == "__main__":
    unittest.main()
