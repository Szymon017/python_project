from collections import deque

from project.cart import Cart


class Order:
    def __init__(self):
        self.queue = deque()

    def add_cart(self, cart: Cart):
        self.queue.append(cart)

    def handle_cart(self):
        if self.queue:
            queue_ = self.queue.popleft()

    def handle_cart_test(self, warehouse):
        print(warehouse)
        if self.queue:
            cart = self.queue[0]
            for product, quantity in cart.cart_items:
                if warehouse.get_product_mock(product) < quantity:
                    self.queue.rotate(-1)
                    return None
            cart = self.queue.popleft()
            for product, quantity in cart.cart_items:
                warehouse.remove_product(product, quantity)
            return cart
    def display_order(self) -> str:
        i = 0
        for cart in self.queue:
            print("Cart" + " " + str(i))
            print(cart.display_cart())
            i += 1
        return ""

    def count_order(self) -> float:
        total_order_price = 0.0
        for cart in self.queue:
            total_order_price += cart.total_sum_with_discount()
        return total_order_price

    def count_order_with_discount(self) -> float:
        total_order_price = 0.0
        discounted_price = 0.0
        for cart in self.queue:
            total_order_price += cart.total_sum_with_discount()

        if total_order_price > 1000:
            discount_amount = total_order_price * 0.20
            discounted_price = total_order_price - discount_amount
            return discounted_price
        return total_order_price

    def count_items(self):
        items = 0
        for cart in self.queue:
            for product, quantity in cart.cart_items:
                items += quantity

        return items


