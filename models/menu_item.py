from abc import ABC, abstractmethod


class MenuItem(ABC):

    def __init__(self, item_id, name, price):
        self.__item_id = item_id
        self.__name = name
        self.price = price

    @property
    def item_id(self):
        return self.__item_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    @abstractmethod
    def calculate_price(self):
        pass

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "price": self.price
        }

    def __str__(self):
        return (
            f"ID: {self.item_id} | "
            f"Name: {self.name} | "
            f"Price: {self.price}"
        )