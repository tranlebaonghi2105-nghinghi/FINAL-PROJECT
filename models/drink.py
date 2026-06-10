from models.menu_item import MenuItem

DRINK_SERVICE_FEE_RATE = 0.05


class Drink(MenuItem):

    def __init__(self, item_id, name, price):
        super().__init__(item_id, name, price)

    def calculate_price(self):
        service_fee = self.price * DRINK_SERVICE_FEE_RATE
        return self.price + service_fee

    def __str__(self):
        return (
            f"[Drink] ID: {self.item_id} | "
            f"Name: {self.name} | "
            f"Base: {self.price:.2f} | "
            f"Price (+5% fee): {self.calculate_price():.2f}"
        )