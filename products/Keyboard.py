from .Product import Product
class Keyboard(Product):
    def __init__(self, name, price,keys,description):
        super().__init__(price, name, description)
        self._keys = None
        self.keys = keys

    @property
    def keys(self):
        return self.keys

    @keys.setter
    def keys(self, value):
        self._keys = value

    def get_info(self):
        return super().get_info() + self.keys

    def get_price_with_delivery(self):
        return self.price + 100