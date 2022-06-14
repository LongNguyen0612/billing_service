from sqlalchemy import inspect
from sqlalchemy.orm import Session
from app.api.factory import response_not_found, response_items
from app.exceptions import ServiceParamsException
from app.models.postgres import Price, Plan, Subscription, Promotion


class PlanService:
    def __init__(self, session: Session, month: str, model_id: str):
        self.__session = session
        self.__model_id = model_id
        self.__month = month

    def execute(self):
        list_plan = []
        if self.__month and not self.__model_id:
            plans = self.__session.query(Plan).all()
            for plan in plans:
                plan_info = {
                    "plan_id": plan.id,
                    "plan_name": plan.plan_name,
                    "price": plan.price.value if plan.price else 0,
                    "months": self.__month
                }

                promotion = self.__session.query(Promotion).filter(Promotion.to_quantity == self.__month).first()
                if not promotion:
                    raise ServiceParamsException(f"Invalid promotion: {promotion}")
                total = int(plan.price.value) if plan.price else 0 * int(self.__month) - int(promotion.to_quantity)/100 * int(plan.price.value) if plan.price else 0

                plan_info.update({"discount": promotion.value,
                                "subtotal": plan.price.value if plan.price else 0,
                                "total": total})
                list_plan.append(plan_info)
        
        elif self.__month and self.__model_id:
            plan = self.__session.query(Plan).filter(Plan.id == self.__model_id).first()
            if not plan:
                raise ServiceParamsException("Invalid plan")
            plan_info_model = {
                    "plan_id": plan.id,
                    "plan_name": plan.plan_name,
                    "price": plan.price.value if plan.price else 0,
                    "months": self.__month
                }

            promotion = self.__session.query(Promotion).filter(Promotion.to_quantity == self.__month).first()
            if not promotion:
                raise ServiceParamsException(f"Invalid promotion: {promotion}")
            sub_total = int(plan.price.value) if plan.price else 0 * int(self.__month)
            total = sub_total - int(promotion.to_quantity)/100 * sub_total


            plan_info_model.update({"discount": promotion.value,
                            "subtotal": sub_total,
                            "total": total})
            list_plan.append(plan_info_model)
            
        return list_plan
