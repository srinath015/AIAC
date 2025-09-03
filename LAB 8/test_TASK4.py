import unittest
from TASK4 import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item_new(self):
        self.cart.add_item("apple", 1.5)
        self.assertIn("apple", self.cart.items)
        self.assertEqual(self.cart.items["apple"], [1.5])

    def test_add_item_existing(self):
        self.cart.add_item("banana", 2.0)
        self.cart.add_item("banana", 3.0)
        self.assertEqual(self.cart.items["banana"], [2.0, 3.0])

    def test_remove_item_existing(self):
        self.cart.add_item("orange", 1.0)
        self.cart.add_item("orange", 2.0)
        self.cart.remove_item("orange")
        self.assertEqual(self.cart.items["orange"], [1.0])
        self.cart.remove_item("orange")
        self.assertNotIn("orange", self.cart.items)

    def test_remove_item_not_existing(self):
        # Should not raise, just print
        self.cart.remove_item("not_in_cart")
        self.assertNotIn("not_in_cart", self.cart.items)

    def test_total_cost_empty(self):
        self.assertEqual(self.cart.total_cost(), 0)

    def test_total_cost_multiple_items(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("banana", 2.0)
        self.cart.add_item("banana", 3.0)
        self.assertEqual(self.cart.total_cost(), 1.5 + 2.0 + 3.0)

    def test_add_item_negative_price(self):
        # Negative price should be handled in main, not here
        self.cart.add_item("apple", -1.0)
        self.assertEqual(self.cart.items["apple"], [-1.0])

if __name__ == "__main__":
    unittest.main()