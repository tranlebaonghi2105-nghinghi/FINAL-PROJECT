class Promotion:

    def __init__(self, promo_code, discount_percent):
        self.__promo_code = promo_code
        self.discount_percent = discount_percent

    @property
    def promo_code(self):
        return self.__promo_code

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
            "promo_code": self.promo_code,
            "discount_percent": self.discount_percent
        }

    def __str__(self):
        return (
            f"Code: {self.promo_code} | "
            f"Discount: {self.discount_percent}%"
        )