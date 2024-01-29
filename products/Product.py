from abc import ABC, abstractmethod


class Product(ABC):

    def __init__(self, price, name, description):
        self._name = None
        self._price = None
        self._description = None
        self.price = price
        self.name = name
        self.description = description

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._price = float(value)
        else:
            raise ValueError("Cena musi być liczbą nieujemną!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Nazwa musi być tekstem!")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self._description = value
        else:
            raise ValueError("Opis musi być tekstem!")


    def get_info(self):
        return self.name + self.price, self.description

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    @abstractmethod
    def get_price_with_delivery(self):
        pass

