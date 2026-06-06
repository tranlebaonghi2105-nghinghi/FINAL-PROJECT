from models.table import Table


class TableService:

    def __init__(self):
        self.tables = []

    def add_table(self, table_id):
        if self.find_by_id(table_id):
            raise ValueError("Table ID already exists.")

        self.tables.append(Table(table_id))

    def get_all_tables(self):
        return self.tables

    def find_by_id(self, table_id):
        for table in self.tables:
            if table.table_id == table_id:
                return table

        return None

    def update_status(self, table_id, status):
        table = self.find_by_id(table_id)

        if table is None:
            raise ValueError("Table not found.")

        table.status = status

    def delete_table(self, table_id):
        table = self.find_by_id(table_id)

        if table is None:
            raise ValueError("Table not found.")

        self.tables.remove(table)

    def to_list_dict(self):
        data = []

        for table in self.tables:
            data.append({
                "table_id": table.table_id,
                "status": table.status
            })

        return data

    def load_from_list_dict(self, data):
        self.tables = []

        for table_data in data:
            table = Table(
                table_data["table_id"],
                table_data["status"]
            )

            self.tables.append(table)