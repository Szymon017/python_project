from .Product import Product

class Guitar(Product):
    def __init__(self, name, price, type, description):
        super().__init__(price, name, description)
        self._type = None
        self.type = type
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if isinstance(value, str):
            self._type = value
        else:
            raise ValueError("Typ musi być tekstem!")

    def get_info(self):
        super().get_info() + self.type

    def get_price_with_delivery(self):
        return self._price + 50

