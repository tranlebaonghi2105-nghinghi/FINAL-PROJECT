from services.menu_service import MenuService
from views.menu_view import MenuView


def main():

    menu_service = MenuService()

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

        elif choice == "0":

            print("Goodbye.")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()