class Promotion:

    def __init__(self, promotion_id, name, discount_percent):
        self.__promotion_id = promotion_id
        self.__name = name
        self.discount_percent = discount_percent

    @property
    def promotion_id(self):
        return self.__promotion_id

    @property
    def name(self):
        return self.__name

    @property
    def discount_percent(self):
        return self.__discount_percent

    @discount_percent.setter
    def discount_percent(self, value):
        if value < 0 or value > 100:
            raise ValueError(
                "Discount must be between 0 and 100."
            )

        self.__discount_percent = value

    def apply_discount(self, amount):
        return amount * (1 - self.discount_percent / 100)

    def to_dict(self):
        return {
            "promotion_id": self.promotion_id,
            "name": self.name,
            "discount_percent": self.discount_percent
        }

    def __str__(self):
        return (
            f"Promotion ID: {self.promotion_id} | "
            f"Name: {self.name} | "
            f"Discount: {self.discount_percent}%"
        )