from products.Guitar import Guitar
from products.Drums import Drums
from cart import Cart
from project.order.order import Order

if __name__ == "__main__":

    guitar_01 = Guitar("Gibson", 1123, "Electric", "")
    guitar_02 = Guitar("Cort", 3211, "Electric", "")

    cart_01 = Cart()
    cart_02 = Cart()
    order_01 = Order()

    cart_01.add_product(guitar_01, 1)
    cart_01.add_product(guitar_02, 1)
    cart_02.add_product(guitar_01, 1)
    cart_02.add_product(guitar_02, 1)

    order_01.add_cart(cart_01)
    order_01.add_cart(cart_02)
    order_01.handle_cart()

    print(order_01.display_order())
    print(order_01.count_order())
    print(order_01.count_order_with_discount())
    order_01.handle_cart_test(2)

