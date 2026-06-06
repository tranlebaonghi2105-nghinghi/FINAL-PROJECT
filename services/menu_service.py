from models.food import Food
from models.drink import Drink
from models.combo import Combo


class MenuService:

    def __init__(self):
        self.menu_items = []

    def add_item(self, item_type, item_id, name, price):
        if self.find_by_id(item_id):
            raise ValueError("Item ID already exists.")

        item = self.create_item_from_data(
            item_type,
            item_id,
            name,
            price
        )

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

    def create_item_from_data(
        self,
        item_type,
        item_id,
        name,
        price
    ):
        if item_type == "Food":
            return Food(item_id, name, price)

        if item_type == "Drink":
            return Drink(item_id, name, price)

        if item_type == "Combo":
            return Combo(item_id, name, price)

        raise ValueError("Invalid item type.")

    def get_item_type(self, item):
        if isinstance(item, Food):
            return "Food"

        if isinstance(item, Drink):
            return "Drink"

        if isinstance(item, Combo):
            return "Combo"

        return "Unknown"

    def to_list_dict(self):
        data = []

        for item in self.menu_items:
            data.append({
                "item_type": self.get_item_type(item),
                "item_id": item.item_id,
                "name": item.name,
                "price": item.price
            })

        return data

    def load_from_list_dict(self, data):
        self.menu_items = []

        for item_data in data:
            item = self.create_item_from_data(
                item_data["item_type"],
                item_data["item_id"],
                item_data["name"],
                item_data["price"]
            )

            self.menu_items.append(item)