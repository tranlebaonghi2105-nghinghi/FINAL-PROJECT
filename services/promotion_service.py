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