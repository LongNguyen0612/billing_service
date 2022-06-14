from app.models import Price
from sqlalchemy.orm import Session


def run(db: Session):
    prices = [
        {
            "plan": "70c3a46f-7341-4bb7-a1a0-3f23a6a1a07e",
            "amount": 500000,
        },
        {
            "plan": "f7e88325-59b7-494c-b1f6-f1e8d58b212d",
            "amount": 600000,
        }
    ]

    for price in prices:
        price_object = Price()
        price_object.value = price.get("amount")
        price_object.plan_id = price.get("plan")
        db.add(price_object)

    db.commit()
