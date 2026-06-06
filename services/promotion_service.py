from models.promotion import Promotion


class PromotionService:

    def __init__(self):

        self.promotions = []

    def add_promotion(
        self,
        promotion_id,
        name,
        discount_percent
    ):

        for promotion in self.promotions:

            if promotion.promotion_id == promotion_id:

                raise Exception(
                    "Promotion ID already exists."
                )

        new_promotion = Promotion(
            promotion_id,
            name,
            discount_percent
        )

        self.promotions.append(
            new_promotion
        )

    def get_all_promotions(self):

        return self.promotions

    def find_by_id(
        self,
        promotion_id
    ):

        for promotion in self.promotions:

            if promotion.promotion_id == promotion_id:

                return promotion

        return None

    def delete_promotion(
        self,
        promotion_id
    ):

        promotion = self.find_by_id(
            promotion_id
        )

        if promotion is None:

            raise Exception(
                "Promotion not found."
            )

        self.promotions.remove(
            promotion
        )

    def to_list_dict(self):

        data = []

        for promotion in self.promotions:

            data.append({
                "promotion_id":
                    promotion.promotion_id,
                "name":
                    promotion.name,
                "discount_percent":
                    promotion.discount_percent
            })

        return data

    def load_from_list_dict(
        self,
        data
    ):

        self.promotions = []

        for promotion_data in data:

            promotion = Promotion(
                promotion_data["promotion_id"],
                promotion_data["name"],
                promotion_data["discount_percent"]
            )

            self.promotions.append(
                promotion
            )