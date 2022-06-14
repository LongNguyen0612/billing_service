from app.models import Plan
from sqlalchemy.orm import Session

from app.utils import generate_uuid


def run(db: Session):
    plans = [
        {
            "name": "email:free",
            "description": "Email for basic",
        },
        {
            "name": "email:basic",
            "description": "Email for basic",
            "price_id": "5370d80f-d88e-4374-9d3d-28971e42c1b9"
        },
        {
            "name": "email:premium",
            "description": "Email for premium",
            "price_id": "0e6dfb77-f7fe-49ba-bab0-8433d21d5eae"
        }
    ]

    for plan in plans:
        plan_object = Plan()
        plan_object.plan_name = plan.get("name")
        plan_object.description = plan.get("description")
        plan_object.price_id = plan.get("price_id")
        db.add(plan_object)

    db.commit()
