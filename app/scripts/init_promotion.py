from app.models import Price, Promotion
from sqlalchemy.orm import Session


def run(db: Session):
    promotions = [
        # {
        #     "plan_id": "1b72ac18-bc18-4cee-8165-ff28c666a1d8",
        #     "from_quantity": "0",
        #     "to_quantity": "10",
        #     "value": "10",
        #     "promotion_type": "discount_percent"
        # },
        # {
        #     "plan_id": "1b72ac18-bc18-4cee-8165-ff28c666a1d8",
        #     "from_quantity": "10",
        #     "to_quantity": "20",
        #     "value": "20",
        #     "promotion_type": "discount_percent"
        # },
        # {
        #     "plan_id": "1b72ac18-bc18-4cee-8165-ff28c666a1d8",
        #     "from_quantity": "20",
        #     "to_quantity": "30",
        #     "value": "30",
        #     "promotion_type": "discount_percent"
        # },
        {
            "plan_id": "7716a376-5552-4c98-a9b2-32d60099681f",
            "from_quantity": "0",
            "to_quantity": "10",
            "value": "10",
            "promotion_type": "discount_percent"
        },
        {
            "plan_id": "7716a376-5552-4c98-a9b2-32d60099681f",
            "from_quantity": "10",
            "to_quantity": "20",
            "value": "20",
            "promotion_type": "discount_percent"
        },
        {
            "plan_id": "7716a376-5552-4c98-a9b2-32d60099681f",
            "from_quantity": "20",
            "to_quantity": "30",
            "value": "30",
            "promotion_type": "discount_percent"
        },
    ]

    for pro in promotions:
        pro_object = Promotion()
        pro_object.value = pro.get("value")
        pro_object.plan_id = pro.get("plan_id")
        pro_object.from_quantity = pro.get("from_quantity")
        pro_object.to_quantity = pro.get("to_quantity")
        pro_object.promotion_type = pro.get("promotion_type")
        db.add(pro_object)

    db.commit()

