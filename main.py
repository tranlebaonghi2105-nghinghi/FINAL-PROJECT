from services.menu_service import MenuService
from services.table_service import TableService
from services.promotion_service import PromotionService
from services.invoice_service import InvoiceService
from services.file_service import FileService
from views.menu_view import MenuView


MENU_FILE = "data/menu.json"
TABLE_FILE = "data/tables.json"
PROMOTION_FILE = "data/promotions.json"
INVOICE_FILE = "data/invoices.json"


def load_all_data(
    menu_service,
    table_service,
    promotion_service,
    invoice_service
):
    menu_service.load_from_list_dict(
        FileService.load_data(MENU_FILE)
    )

    table_service.load_from_list_dict(
        FileService.load_data(TABLE_FILE)
    )

    promotion_service.load_from_list_dict(
        FileService.load_data(PROMOTION_FILE)
    )

    invoice_service.load_from_list_dict(
        FileService.load_data(INVOICE_FILE)
    )


def save_all_data(
    menu_service,
    table_service,
    promotion_service,
    invoice_service
):
    FileService.save_data(
        MENU_FILE,
        menu_service.to_list_dict()
    )

    FileService.save_data(
        TABLE_FILE,
        table_service.to_list_dict()
    )

    FileService.save_data(
        PROMOTION_FILE,
        promotion_service.to_list_dict()
    )

    FileService.save_data(
        INVOICE_FILE,
        invoice_service.to_list_dict()
    )


def main():

    menu_service = MenuService()
    table_service = TableService()
    promotion_service = PromotionService()
    invoice_service = InvoiceService()

    load_all_data(
        menu_service,
        table_service,
        promotion_service,
        invoice_service
    )

    while True:

        MenuView.display_main_menu()

        choice = MenuView.get_choice()

        if choice == "1":

            item_type = input(
                "Enter item type (Food/Drink/Combo): "
            )

            item_id = input(
                "Enter item ID: "
            )

            name = input(
                "Enter item name: "
            )

            price = float(
                input("Enter item price: ")
            )

            try:

                menu_service.add_item(
                    item_type,
                    item_id,
                    name,
                    price
                )

                MenuView.show_message(
                    "Item added successfully."
                )

            except Exception as error:

                MenuView.show_message(error)

        elif choice == "2":

            MenuView.display_items(
                menu_service.get_all_items()
            )

        elif choice == "3":

            keyword = input(
                "Enter item name: "
            )

            result = menu_service.search_by_name(
                keyword
            )

            MenuView.display_items(result)

        elif choice == "4":

            item_id = input(
                "Enter item ID: "
            )

            new_price = float(
                input("Enter new price: ")
            )

            try:

                menu_service.update_item(
                    item_id,
                    new_price
                )

                MenuView.show_message(
                    "Updated successfully."
                )

            except Exception as error:

                MenuView.show_message(error)

        elif choice == "5":

            item_id = input(
                "Enter item ID: "
            )

            try:

                menu_service.delete_item(
                    item_id
                )

                MenuView.show_message(
                    "Deleted successfully."
                )

            except Exception as error:

                MenuView.show_message(error)

        elif choice == "6":

            MenuView.display_items(
                menu_service.sort_by_price_ascending()
            )

        elif choice == "7":

            MenuView.display_items(
                menu_service.sort_by_price_descending()
            )

        elif choice == "8":

            table_id = input(
                "Enter table ID: "
            )

            try:

                table_service.add_table(
                    table_id
                )

                print(
                    "Table added successfully."
                )

            except Exception as error:

                print(error)

        elif choice == "9":

            tables = table_service.get_all_tables()

            if len(tables) == 0:

                print("No tables found.")

            else:

                for table in tables:

                    print(table)

        elif choice == "10":

            table_id = input(
                "Enter table ID: "
            )

            status = input(
                "Enter status (Available/Occupied): "
            )

            try:

                table_service.update_status(
                    table_id,
                    status
                )

                print(
                    "Status updated successfully."
                )

            except Exception as error:

                print(error)

        elif choice == "11":

            promotion_id = input(
                "Enter promotion ID: "
            )

            name = input(
                "Enter promotion name: "
            )

            discount_percent = float(
                input("Enter discount percent: ")
            )

            try:

                promotion_service.add_promotion(
                    promotion_id,
                    name,
                    discount_percent
                )

                print(
                    "Promotion added successfully."
                )

            except Exception as error:

                print(error)

        elif choice == "12":

            promotions = promotion_service.get_all_promotions()

            if len(promotions) == 0:

                print("No promotions found.")

            else:

                for promotion in promotions:

                    print(promotion)

        elif choice == "13":

            promotion_id = input(
                "Enter promotion ID: "
            )

            try:

                promotion_service.delete_promotion(
                    promotion_id
                )

                print(
                    "Promotion deleted successfully."
                )

            except Exception as error:

                print(error)

        elif choice == "14":

            invoice_id = input(
                "Enter invoice ID: "
            )

            table_id = input(
                "Enter table ID: "
            )

            table = table_service.find_by_id(
                table_id
            )

            if table is None:

                print("Table not found.")

            else:

                try:

                    invoice_service.create_invoice(
                        invoice_id,
                        table_id
                    )

                    table_service.update_status(
                        table_id,
                        "Occupied"
                    )

                    print(
                        "Invoice created successfully."
                    )

                except Exception as error:

                    print(error)

        elif choice == "15":

            invoice_id = input(
                "Enter invoice ID: "
            )

            item_id = input(
                "Enter item ID: "
            )

            item = menu_service.find_by_id(
                item_id
            )

            if item is None:

                print("Item not found.")

            else:

                try:

                    invoice_service.add_item_to_invoice(
                        invoice_id,
                        item
                    )

                    print(
                        "Item added to invoice successfully."
                    )

                except Exception as error:

                    print(error)

        elif choice == "16":

            invoice_id = input(
                "Enter invoice ID: "
            )

            promotion_id = input(
                "Enter promotion ID: "
            )

            promotion = promotion_service.find_by_id(
                promotion_id
            )

            if promotion is None:

                print("Promotion not found.")

            else:

                try:

                    invoice_service.apply_promotion_to_invoice(
                        invoice_id,
                        promotion
                    )

                    print(
                        "Promotion applied successfully."
                    )

                except Exception as error:

                    print(error)

        elif choice == "17":

            invoices = invoice_service.get_all_invoices()

            if len(invoices) == 0:

                print("No invoices found.")

            else:

                for invoice in invoices:

                    print(invoice)

        elif choice == "0":

            save_all_data(
                menu_service,
                table_service,
                promotion_service,
                invoice_service
            )

            print("Data saved successfully.")
            print("Goodbye.")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()