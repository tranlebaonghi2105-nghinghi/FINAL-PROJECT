from prettytable import PrettyTable


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
        print("8. Add Table")
        print("9. View Tables")
        print("10. Update Table Status")
        print("11. Add Promotion")
        print("12. View Promotions")
        print("13. Delete Promotion")
        print("14. Create Invoice")
        print("15. Add Item To Invoice")
        print("16. Apply Promotion To Invoice")
        print("17. View Invoices")
        print("18. Total Revenue")
        print("19. Number Of Invoices")
        print("20. Most Expensive Item")
        print("21. Statistics By Type")
        print("22. Export Invoices To CSV")
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

        table = PrettyTable()

        table.field_names = [
            "Item ID",
            "Name",
            "Price"
        ]

        for item in items:

            table.add_row([
                item.item_id,
                item.name,
                f"{item.calculate_price():.2f}"
            ])

        print(table)

    @staticmethod
    def display_promotions(promotions):

        if len(promotions) == 0:

            print("No promotions found.")
            return

        table = PrettyTable()

        table.field_names = [
            "Promotion ID",
            "Name",
            "Discount (%)"
        ]

        for promotion in promotions:

            table.add_row([
                promotion.promotion_id,
                promotion.name,
                f"{promotion.discount_percent:.2f}"
            ])

        print(table)

    @staticmethod
    def show_statistics(stats):

        print("\n" + "=" * 50)
        print("STATISTICS BY ITEM TYPE")
        print("=" * 50)

        table = PrettyTable()

        table.field_names = [
            "Item Type",
            "Count",
            "Total Revenue"
        ]

        for item_type, data in stats.items():

            table.add_row([
                item_type,
                data["count"],
                f"{data['revenue']:.2f}"
            ])

        print(table)