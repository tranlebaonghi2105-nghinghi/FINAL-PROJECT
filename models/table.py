class Table:

    def __init__(self, table_id, status="Available"):
        self.__table_id = table_id
        self.status = status

    @property
    def table_id(self):
        return self.__table_id

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if value not in ["Available", "Occupied"]:
            raise ValueError("Invalid table status.")
        self.__status = value

    def to_dict(self):
        return {
            "table_id": self.table_id,
            "status": self.status
        }

    def __str__(self):
        return (
            f"Table ID: {self.table_id} | "
            f"Status: {self.status}"
        )