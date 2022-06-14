from app.api.services.order_services._order_generated import OrderSettable
from sqlalchemy.orm import Session

from app.api.services.order_services.oder_settable._order_settable_service import \
    OrderSettableService
from app.exceptions import ServiceParamsException
from app.models import Subscription, Promotion, Plan
from app.utils import generate_uuid
from app.utils.billing_time import get_today, get_after_month


class OrderGenerateService(OrderSettable):
    def __init__(self, payload: dict, session: Session):
        self.__session = session
        self.__payload = payload
        self.__subscription_settable = OrderSettableService()

    def set_result(self, subscription: Subscription):
        self.__subscription_settable.set_result(subscription)

    def generate(self) -> Subscription:
        subscription = self.__subscription_settable.generate()

        promotion = self.__session.query(Promotion).filter(Promotion.to_quantity == self.__payload.get("month")).first()
        if not promotion:
            raise ServiceParamsException("Invalid promotion")

        plan = self.__session.query(Plan).filter(Plan.plan_name == self.__payload.get("plan_name")).first()
        if not plan:
            raise ServiceParamsException("Invalid plan")

        subscription.id = generate_uuid()
        subscription.plan_id = plan.id
        subscription.promotion_id = promotion.id
        subscription.price_id = plan.price_id
        subscription.start_time = get_today()
        subscription.status = 'active'
        subscription.account_id = self.__payload.get("account_id")
        subscription.end_time = get_after_month()
        subscription.month = self.__payload.get("month")
        subscription.order_id = self.__payload.get("order_id")

        return subscription
