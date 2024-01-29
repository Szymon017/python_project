from .Product import Product

class Drums(Product):
    def __init__(self, name, price, description):
        super().__init__(price, name, description)

    def get_price_with_delivery(self):
        return self.price + 320