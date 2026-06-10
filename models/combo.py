from models.menu_item import MenuItem

COMBO_DISCOUNT_RATE = 0.10


class Combo(MenuItem):

    def __init__(self, item_id, name, price):
        super().__init__(item_id, name, price)

    def calculate_price(self):
        discount = self.price * COMBO_DISCOUNT_RATE
        return self.price - discount

    def __str__(self):
        return (
            f"[Combo] ID: {self.item_id} | "
            f"Name: {self.name} | "
            f"Base: {self.price:.2f} | "
            f"Price (-10% combo): {self.calculate_price():.2f}"
        )