from models.invoice import Invoice


class InvoiceService:

    def __init__(self):
        self.invoices = []

    def create_invoice(
        self,
        invoice_id,
        table_id
    ):
        if self.find_by_id(invoice_id):
            raise ValueError("Invoice ID already exists.")

        invoice = Invoice(
            invoice_id,
            table_id
        )

        self.invoices.append(invoice)

        return invoice

    def get_all_invoices(self):
        return self.invoices

    def find_by_id(self, invoice_id):
        for invoice in self.invoices:
            if invoice.invoice_id == invoice_id:
                return invoice

        return None

    def add_item_to_invoice(
        self,
        invoice_id,
        item
    ):
        invoice = self.find_by_id(invoice_id)

        if invoice is None:
            raise ValueError("Invoice not found.")

        invoice.add_item(item)

    def apply_promotion_to_invoice(
        self,
        invoice_id,
        promotion
    ):
        invoice = self.find_by_id(invoice_id)

        if invoice is None:
            raise ValueError("Invoice not found.")

        invoice.apply_promotion(promotion)

    def delete_invoice(self, invoice_id):
        invoice = self.find_by_id(invoice_id)

        if invoice is None:
            raise ValueError("Invoice not found.")

        self.invoices.remove(invoice)