from prettytable import PrettyTable


class Invoice:

    def __init__(
        self,
        invoice_id,
        table_id,
        items=None,
        promotion=None
    ):
        self.__invoice_id = invoice_id
        self.__table_id = table_id
        self.items = items if items else []
        self.promotion = promotion

    @property
    def invoice_id(self):
        return self.__invoice_id

    @property
    def table_id(self):
        return self.__table_id

    def add_item(self, item):
        self.items.append(item)

    def apply_promotion(self, promotion):
        self.promotion = promotion

    def calculate_subtotal(self):
        subtotal = 0

        for item in self.items:
            subtotal += item.calculate_price()

        return subtotal

    def calculate_discount_amount(self):
        if self.promotion is None:
            return 0

        return self.calculate_subtotal() * (
            self.promotion.discount_percent / 100
        )

    def calculate_total(self):
        return (
            self.calculate_subtotal()
            - self.calculate_discount_amount()
        )

    def to_dict(self):
        return {
            "invoice_id": self.invoice_id,
            "table_id": self.table_id,
            "items": [
                item.to_dict()
                for item in self.items
            ],
            "promotion": (
                self.promotion.to_dict()
                if self.promotion
                else None
            ),
            "subtotal": self.calculate_subtotal(),
            "discount": self.calculate_discount_amount(),
            "total": self.calculate_total()
        }

    def __str__(self):
        invoice_table = PrettyTable()

        invoice_table.field_names = [
            "Item ID",
            "Name",
            "Price"
        ]

        if len(self.items) == 0:
            invoice_table.add_row([
                "-",
                "No items in invoice",
                "-"
            ])
        else:
            for item in self.items:
                invoice_table.add_row([
                    item.item_id,
                    item.name,
                    item.calculate_price()
                ])

        summary_table = PrettyTable()

        summary_table.field_names = [
            "Description",
            "Value"
        ]

        summary_table.add_row([
            "Invoice ID",
            self.invoice_id
        ])

        summary_table.add_row([
            "Table ID",
            self.table_id
        ])

        summary_table.add_row([
            "Subtotal",
            self.calculate_subtotal()
        ])

        summary_table.add_row([
            "Discount",
            self.calculate_discount_amount()
        ])

        summary_table.add_row([
            "Total",
            self.calculate_total()
        ])

        if self.promotion:
            summary_table.add_row([
                "Promotion",
                (
                    f"{self.promotion.name} "
                    f"({self.promotion.discount_percent}%)"
                )
            ])
        else:
            summary_table.add_row([
                "Promotion",
                "None"
            ])

        text = "\n"
        text += "=" * 50 + "\n"
        text += "INVOICE DETAIL\n"
        text += "=" * 50 + "\n"
        text += str(summary_table) + "\n"
        text += str(invoice_table) + "\n"
        text += "=" * 50

        return text