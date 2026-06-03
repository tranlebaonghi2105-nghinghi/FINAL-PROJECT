from models.menu_item import MenuItem


class Food(MenuItem):

    def __init__(self, item_id, name, price):
        super().__init__(item_id, name, price)

    def calculate_price(self):
        return self.price