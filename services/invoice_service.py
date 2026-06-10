import csv
import os
from models.invoice import Invoice
from models.food import Food
from models.drink import Drink
from models.combo import Combo
from models.promotion import Promotion


class InvoiceService:

    def __init__(self):
        self.invoices = []

    def create_invoice(self, invoice_id, table_id):
        if self.find_by_id(invoice_id):
            raise ValueError("Invoice ID already exists.")

        invoice = Invoice(invoice_id, table_id)
        self.invoices.append(invoice)
        return invoice

    def get_all_invoices(self):
        return self.invoices

    def find_by_id(self, invoice_id):
        for invoice in self.invoices:
            if invoice.invoice_id == invoice_id:
                return invoice
        return None

    def add_item_to_invoice(self, invoice_id, item):
        invoice = self.find_by_id(invoice_id)

        if invoice is None:
            raise ValueError("Invoice not found.")

        invoice.add_item(item)

    def apply_promotion_to_invoice(self, invoice_id, promotion):
        invoice = self.find_by_id(invoice_id)

        if invoice is None:
            raise ValueError("Invoice not found.")

        invoice.apply_promotion(promotion)

    def delete_invoice(self, invoice_id):
        invoice = self.find_by_id(invoice_id)

        if invoice is None:
            raise ValueError("Invoice not found.")

        self.invoices.remove(invoice)

    def get_total_revenue(self):
        total = 0

        for invoice in self.invoices:
            total += invoice.calculate_total()

        return total

    def get_invoice_count(self):
        return len(self.invoices)

    def get_most_expensive_item(self):
        most_expensive_item = None

        for invoice in self.invoices:
            for item in invoice.items:
                if most_expensive_item is None:
                    most_expensive_item = item
                elif item.calculate_price() > most_expensive_item.calculate_price():
                    most_expensive_item = item

        return most_expensive_item

    def get_statistics_by_type(self):
        stats = {
            "Food": {"count": 0, "revenue": 0.0},
            "Drink": {"count": 0, "revenue": 0.0},
            "Combo": {"count": 0, "revenue": 0.0}
        }

        for invoice in self.invoices:
            for item in invoice.items:
                item_type = self.get_item_type(item)

                if item_type in stats:
                    stats[item_type]["count"] += 1
                    stats[item_type]["revenue"] += item.calculate_price()

        return stats

    def export_to_csv(self):
        if not os.path.exists("data"):
            os.makedirs("data")

        filename = "data/invoices_export.csv"

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Invoice ID",
                "Table ID",
                "Item ID",
                "Item Name",
                "Item Type",
                "Item Price",
                "Promotion",
                "Discount (%)",
                "Subtotal",
                "Total"
            ])

            for invoice in self.invoices:
                promotion_name = (
                    invoice.promotion.name
                    if invoice.promotion
                    else "None"
                )

                discount_percent = (
                    invoice.promotion.discount_percent
                    if invoice.promotion
                    else 0
                )

                if len(invoice.items) == 0:
                    writer.writerow([
                        invoice.invoice_id,
                        invoice.table_id,
                        "-",
                        "-",
                        "-",
                        "-",
                        promotion_name,
                        discount_percent,
                        invoice.calculate_subtotal(),
                        invoice.calculate_total()
                    ])
                else:
                    for item in invoice.items:
                        writer.writerow([
                            invoice.invoice_id,
                            invoice.table_id,
                            item.item_id,
                            item.name,
                            self.get_item_type(item),
                            f"{item.calculate_price():.2f}",
                            promotion_name,
                            discount_percent,
                            f"{invoice.calculate_subtotal():.2f}",
                            f"{invoice.calculate_total():.2f}"
                        ])

        return filename

    def get_item_type(self, item):
        if isinstance(item, Food):
            return "Food"

        if isinstance(item, Drink):
            return "Drink"

        if isinstance(item, Combo):
            return "Combo"

        return "Unknown"

    def create_item_from_data(self, item_data):
        item_type = item_data["item_type"]
        item_id = item_data["item_id"]
        name = item_data["name"]
        price = item_data["price"]

        if item_type == "Food":
            return Food(item_id, name, price)

        if item_type == "Drink":
            return Drink(item_id, name, price)

        if item_type == "Combo":
            return Combo(item_id, name, price)

        raise ValueError("Invalid item type.")

    def create_promotion_from_data(self, promotion_data):
        if promotion_data is None:
            return None

        return Promotion(
            promotion_data["promotion_id"],
            promotion_data["name"],
            promotion_data["discount_percent"]
        )

    def to_list_dict(self):
        data = []

        for invoice in self.invoices:
            invoice_data = {
                "invoice_id": invoice.invoice_id,
                "table_id": invoice.table_id,
                "items": [],
                "promotion": None
            }

            for item in invoice.items:
                invoice_data["items"].append({
                    "item_type": self.get_item_type(item),
                    "item_id": item.item_id,
                    "name": item.name,
                    "price": item.price
                })

            if invoice.promotion is not None:
                invoice_data["promotion"] = {
                    "promotion_id": invoice.promotion.promotion_id,
                    "name": invoice.promotion.name,
                    "discount_percent": invoice.promotion.discount_percent
                }

            data.append(invoice_data)

        return data

    def load_from_list_dict(self, data):
        self.invoices = []

        for invoice_data in data:
            items = []

            for item_data in invoice_data["items"]:
                item = self.create_item_from_data(item_data)
                items.append(item)

            promotion = self.create_promotion_from_data(
                invoice_data["promotion"]
            )

            invoice = Invoice(
                invoice_data["invoice_id"],
                invoice_data["table_id"],
                items,
                promotion
            )

            self.invoices.append(invoice)