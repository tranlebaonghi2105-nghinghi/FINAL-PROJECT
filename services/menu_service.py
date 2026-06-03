from models.food import Food
from models.drink import Drink
from models.combo import Combo


class MenuService:

    def __init__(self):
        self.menu_items = []

    def add_item(self, item_type, item_id, name, price):
        if self.find_by_id(item_id):
            raise ValueError("Item ID already exists.")

        if item_type == "Food":
            item = Food(item_id, name, price)
        elif item_type == "Drink":
            item = Drink(item_id, name, price)
        elif item_type == "Combo":
            item = Combo(item_id, name, price)
        else:
            raise ValueError("Invalid item type.")

        self.menu_items.append(item)

    def get_all_items(self):
        return self.menu_items

    def find_by_id(self, item_id):
        for item in self.menu_items:
            if item.item_id == item_id:
                return item
        return None

    def search_by_name(self, name):
        result = []

        for item in self.menu_items:
            if name.lower() in item.name.lower():
                result.append(item)

        return result

    def update_item(self, item_id, new_price):
        item = self.find_by_id(item_id)

        if item is None:
            raise ValueError("Item not found.")

        item.price = new_price

    def delete_item(self, item_id):
        item = self.find_by_id(item_id)

        if item is None:
            raise ValueError("Item not found.")

        self.menu_items.remove(item)

    def sort_by_price_ascending(self):
        return sorted(
            self.menu_items,
            key=lambda item: item.price
        )

    def sort_by_price_descending(self):
        return sorted(
            self.menu_items,
            key=lambda item: item.price,
            reverse=True
        )