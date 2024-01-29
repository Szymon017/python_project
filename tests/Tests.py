import unittest
from unittest import TestCase
from unittest.mock import Mock, MagicMock

from project.cart import Cart
from project.order.order import Order
from project.products.Drums import Drums
from project.products.Guitar import Guitar


class Tests(TestCase):
    def setUp(self):
        self.mock_inventory = Mock()

    def test_handle_empty_queue(self):
        order_queue = Order()
        order_queue.add_cart(self.mock_inventory)
        result = order_queue.handle_cart()
        self.assertIsNone(result, "Queue is empty")

    def test_if_there_is_only_one_cart(self):
        order_queue = Order()
        cart_01 = Cart()
        guitar_01 = Guitar("Guitar_01", 799, "classical", "best for begginers")
        guitar_02 = Guitar("Guitar_02", 1599, "electrical", "best for metalheads")
        cart_01.add_product(guitar_01, 1)
        cart_01.add_product(guitar_02, 2)

        order_queue.add_cart(cart_01)

        self.mock_inventory.get_product_mock = MagicMock(
            side_effect=[1, 2]
        )

        result = order_queue.handle_cart_test(self.mock_inventory)

        self.assertEqual(result, cart_01)

    def test_if_there_is_no_product(self):
        product = Guitar("Guitar_01", 799, "classical", "best for begginers")
        cart = Cart()
        cart.add_product(product, 1)
        order_queue = Order()

        order_queue.add_cart(cart)
        self.mock_inventory.get_product_mock.return_value = 0
        handle_order = order_queue.handle_cart_test(self.mock_inventory)
        self.assertIsNone(handle_order)

    def test_discount(self):
        guitar_01 = Guitar("Guitar_01", 600, "classical", "")
        guitar_02 = Guitar("Guitar_02", 1200, "classical", "")
        cart = Cart()
        cart.add_product(guitar_02, 1)
        cart.add_product(guitar_01, 1)

        # rabat 20% z guitar_01 wynosi 960 zł
        # rabat 5% z guitar_02 wynosi 570 zł
        # łączna cena 1530
        price = cart.total_sum_with_discount()
        print(f"Total without discount: {cart.sum_of_items()}")
        print(f"Total with discount: {cart.total_sum_with_discount()}")

        self.assertEqual(price, 1530)

    def test_discount_on_order(self):
        guitar_01 = Guitar("Guitar_01", 600, "classical", "")
        guitar_02 = Guitar("Guitar_02", 1200, "classical", "")
        cart = Cart()
        cart.add_product(guitar_02, 1)
        cart.add_product(guitar_01, 1)
        order_ = Order()
        order_.add_cart(cart)
        # cena z rabatami na produkty wynosi 1530
        # > 1000 rabat 20% = 1224
        result = order_.count_order_with_discount()
        self.assertEqual(result, 1224)



if __name__ == '__main__':
    unittest.main()