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


def load_all_data(menu_service, table_service, promotion_service, invoice_service):
    menu_service.load_from_list_dict(FileService.load_data(MENU_FILE))
    table_service.load_from_list_dict(FileService.load_data(TABLE_FILE))
    promotion_service.load_from_list_dict(FileService.load_data(PROMOTION_FILE))
    invoice_service.load_from_list_dict(FileService.load_data(INVOICE_FILE))


def save_all_data(menu_service, table_service, promotion_service, invoice_service):
    FileService.save_data(MENU_FILE, menu_service.to_list_dict())
    FileService.save_data(TABLE_FILE, table_service.to_list_dict())
    FileService.save_data(PROMOTION_FILE, promotion_service.to_list_dict())
    FileService.save_data(INVOICE_FILE, invoice_service.to_list_dict())


def run_cli(menu_service, table_service, promotion_service, invoice_service):
    while True:
        MenuView.display_main_menu()
        choice = MenuView.get_choice()

        if choice == "1":
            try:
                item_type = input("Enter item type (Food/Drink/Combo): ")
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                menu_service.add_item(item_type, item_id, name, price)
                MenuView.show_message("Item added successfully.")
            except ValueError as error:
                MenuView.show_message(f"Invalid input: {error}")
            except Exception as error:
                MenuView.show_message(error)

        elif choice == "2":
            MenuView.display_items(menu_service.get_all_items())

        elif choice == "3":
            keyword = input("Enter item name: ")
            result = menu_service.search_by_name(keyword)
            MenuView.display_items(result)

        elif choice == "4":
            try:
                item_id = input("Enter item ID: ")
                new_price = float(input("Enter new price: "))
                menu_service.update_item(item_id, new_price)
                MenuView.show_message("Updated successfully.")
            except ValueError as error:
                MenuView.show_message(f"Invalid input: {error}")
            except Exception as error:
                MenuView.show_message(error)

        elif choice == "5":
            item_id = input("Enter item ID: ")
            try:
                menu_service.delete_item(item_id)
                MenuView.show_message("Deleted successfully.")
            except Exception as error:
                MenuView.show_message(error)

        elif choice == "6":
            MenuView.display_items(menu_service.sort_by_price_ascending())

        elif choice == "7":
            MenuView.display_items(menu_service.sort_by_price_descending())

        elif choice == "8":
            table_id = input("Enter table ID: ")
            try:
                table_service.add_table(table_id)
                MenuView.show_message("Table added successfully.")
            except Exception as error:
                MenuView.show_message(error)

        elif choice == "9":
            tables = table_service.get_all_tables()
            if len(tables) == 0:
                MenuView.show_message("No tables found.")
            else:
                for table in tables:
                    print(table)

        elif choice == "10":
            table_id = input("Enter table ID: ")
            status = input("Enter status (Available/Occupied): ")
            try:
                table_service.update_status(table_id, status)
                MenuView.show_message("Status updated successfully.")
            except Exception as error:
                MenuView.show_message(error)

        elif choice == "11":
            try:
                promotion_id = input("Enter promotion ID: ")
                name = input("Enter promotion name: ")
                discount_percent = float(input("Enter discount percent: "))
                promotion_service.add_promotion(promotion_id, name, discount_percent)
                MenuView.show_message("Promotion added successfully.")
            except ValueError as error:
                MenuView.show_message(f"Invalid input: {error}")
            except Exception as error:
                MenuView.show_message(error)

        elif choice == "12":
            MenuView.display_promotions(promotion_service.get_all_promotions())

        elif choice == "13":
            promotion_id = input("Enter promotion ID: ")
            try:
                promotion_service.delete_promotion(promotion_id)
                MenuView.show_message("Promotion deleted successfully.")
            except Exception as error:
                MenuView.show_message(error)

        elif choice == "14":
            invoice_id = input("Enter invoice ID: ")
            table_id = input("Enter table ID: ")
            table = table_service.find_by_id(table_id)
            if table is None:
                MenuView.show_message("Table not found.")
            else:
                try:
                    invoice_service.create_invoice(invoice_id, table_id)
                    table_service.update_status(table_id, "Occupied")
                    MenuView.show_message("Invoice created successfully.")
                except Exception as error:
                    MenuView.show_message(error)

        elif choice == "15":
            invoice_id = input("Enter invoice ID: ")
            item_id = input("Enter item ID: ")
            item = menu_service.find_by_id(item_id)
            if item is None:
                MenuView.show_message("Item not found.")
            else:
                try:
                    invoice_service.add_item_to_invoice(invoice_id, item)
                    MenuView.show_message("Item added to invoice successfully.")
                except Exception as error:
                    MenuView.show_message(error)

        elif choice == "16":
            invoice_id = input("Enter invoice ID: ")
            promotion_id = input("Enter promotion ID: ")
            promotion = promotion_service.find_by_id(promotion_id)
            if promotion is None:
                MenuView.show_message("Promotion not found.")
            else:
                try:
                    invoice_service.apply_promotion_to_invoice(invoice_id, promotion)
                    MenuView.show_message("Promotion applied successfully.")
                except Exception as error:
                    MenuView.show_message(error)

        elif choice == "17":
            invoices = invoice_service.get_all_invoices()
            if len(invoices) == 0:
                MenuView.show_message("No invoices found.")
            else:
                for invoice in invoices:
                    print(invoice)

        elif choice == "18":
            total_revenue = invoice_service.get_total_revenue()
            MenuView.show_message(f"Total Revenue: {total_revenue:.2f}")

        elif choice == "19":
            invoice_count = invoice_service.get_invoice_count()
            MenuView.show_message(f"Number Of Invoices: {invoice_count}")

        elif choice == "20":
            item = invoice_service.get_most_expensive_item()
            if item is None:
                MenuView.show_message("No item found in invoices.")
            else:
                print("Most Expensive Item:")
                print(f"ID: {item.item_id}")
                print(f"Name: {item.name}")
                print(f"Price: {item.calculate_price():.2f}")

        elif choice == "21":
            MenuView.show_statistics(invoice_service.get_statistics_by_type())

        elif choice == "22":
            filename = invoice_service.export_to_csv()
            MenuView.show_message(f"Exported successfully to: {filename}")

        elif choice == "0":
            save_all_data(menu_service, table_service, promotion_service, invoice_service)
            MenuView.show_message("Data saved successfully.")
            MenuView.show_message("Goodbye.")
            break

        else:
            MenuView.show_message("Invalid choice.")


def run_gui(menu_service, table_service, promotion_service, invoice_service):
    from views.gui_view import GUIView

    def on_exit():
        save_all_data(menu_service, table_service, promotion_service, invoice_service)

    app = GUIView(
        menu_service,
        table_service,
        promotion_service,
        invoice_service,
        on_exit
    )
    app.run()


def main():
    menu_service = MenuService()
    table_service = TableService()
    promotion_service = PromotionService()
    invoice_service = InvoiceService()

    load_all_data(menu_service, table_service, promotion_service, invoice_service)

    print("\n========================================")
    print("  CAFE MANAGEMENT SYSTEM")
    print("========================================")
    print("  1. Run GUI (Graphical Interface)")
    print("  2. Run CLI (Command Line Interface)")
    print("========================================")
    mode = input("Choose mode (1/2): ").strip()

    if mode == "1":
        run_gui(menu_service, table_service, promotion_service, invoice_service)
    else:
        run_cli(menu_service, table_service, promotion_service, invoice_service)


if __name__ == "__main__":
    main()