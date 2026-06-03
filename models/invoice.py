from models.promotion import Promotion


class Invoice:

    def __init__(
        self,
        invoice_id,
        table_id,
        items=None,
        promotion=None
    ):
        self.__invoice_id = invoice_id
        self.table_id = table_id
        self.items = items if items else []
        self.promotion = promotion

    @property
    def invoice_id(self):
        return self.__invoice_id

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item.calculate_price()

        if self.promotion:
            total = self.promotion.apply_discount(total)

        return total

    def to_dict(self):
        return {
            "invoice_id": self.invoice_id,
            "table_id": self.table_id,
            "items": [
                item.to_dict()
                for item in self.items
            ],
            "total": self.calculate_total()
        }

    def __str__(self):
        return (
            f"Invoice ID: {self.invoice_id}\n"
            f"Table ID: {self.table_id}\n"
            f"Items: {len(self.items)}\n"
            f"Total: {self.calculate_total()}"
        )