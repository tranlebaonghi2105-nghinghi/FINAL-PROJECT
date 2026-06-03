from services.menu_service import MenuService
from services.table_service import TableService
from views.menu_view import MenuView


def main():

    menu_service = MenuService()
    table_service = TableService()

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

        elif choice == "0":

            print("Goodbye.")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()