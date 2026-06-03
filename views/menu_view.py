class MenuView:

    @staticmethod
    def display_main_menu():

        print("\n" + "=" * 50)
        print("CAFE MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Menu Item")
        print("2. View Menu")
        print("3. Search Menu Item")
        print("4. Update Menu Item")
        print("5. Delete Menu Item")
        print("6. Sort Menu Ascending")
        print("7. Sort Menu Descending")
        print("0. Exit")

        print("=" * 50)

    @staticmethod
    def get_choice():

        return input("Enter your choice: ")

    @staticmethod
    def show_message(message):

        print(message)

    @staticmethod
    def display_items(items):

        if len(items) == 0:
            print("No data found.")
            return

        for item in items:
            print(item)