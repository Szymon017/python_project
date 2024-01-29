from typing import List, Tuple
from project.products.Product import Product


class Cart:
    def __init__(self):
        self.cart_items: List[Tuple[Product, int]] = []

    def add_product(self, product: Product, quantity: int) -> None:
        for i, item in enumerate(self.cart_items):
            existing_product, existing_quantity = item
            if existing_product == product:
                updated_quantity = existing_quantity + quantity
                self.cart_items[i] = (existing_product, updated_quantity)
                break
        else:
            self.cart_items.append((product, quantity))

    def display_cart(self):
        cart_info = []
        for item in self.cart_items:
            cart_info.append(f"{item[0].name}: {item[1]}")
        return cart_info

    def remove_product(self, product: Product, quantity: int = 0) -> None:
        for i, item in enumerate(self.cart_items):
            existing_product, existing_quantity = item
            if existing_product.name == product.name:
                if quantity == 0 or quantity >= existing_quantity:
                    del self.cart_items[i]
                else:
                    updated_quantity = existing_quantity - quantity
                    self.cart_items[i] = (existing_product, updated_quantity)
                break
        else:
            pass

    def sum(self):
        return sum(product.price * quantity for product, quantity in self.cart_items)

    def total_items(self) -> int:
        total = sum(quantity for _, quantity in self.cart_items)
        return total

    def sum_of_items(self) -> float:
        total_price = 0.0
        for product, quantity in self.cart_items:
            item_price = product.price * quantity
            total_price += item_price
            print(f"{product.name}, {quantity}, {item_price} zł")
        return total_price

    def sum_of_items_with_discount(self, discount) -> float:
        total_price = 0.0
        for product, quantity in self.cart_items:
            item_price = product.calculate_discount(discount)
            total_price += item_price
            print(f"{product.name}, {quantity}, {item_price} zł")
        return total_price

    def discount(self, total_price) -> float:
        discount = 0.0
        if total_price > 1000:
            discount = 0.2  # 20%
        elif total_price > 500:
            discount = 0.05  # 5%
        else:
            discount = 0.0

        discount_amount = total_price * discount
        discounted_price = total_price - discount_amount
        return discounted_price

    def discount_of_item(self) -> None:
        for product, quantity in self.cart_items:
            total = self.discount(product.price*quantity)
            print(f"{product.name}, {total}")

    def total_sum_with_discount(self) -> float:
        total_price = 0.0
        for product, quantity in self.cart_items:
            total_price += self.discount(product.price * quantity)
        return total_price

