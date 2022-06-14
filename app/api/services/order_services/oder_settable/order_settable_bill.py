from app.api.services.order_services._order_generated import OrderSettable
from sqlalchemy.orm import Session

from app.api.services.order_services.oder_settable._order_settable_service import \
    OrderSettableService
from app.exceptions import ServiceParamsException
from app.models import Subscription, Bill, Promotion, Price, Plan
from app.utils import generate_uuid


class OrderSettableBillService(OrderSettable):
    def __init__(self, payload: dict, session: Session):
        self.__session = session
        self.__payload = payload
        self.__subscription_settable = OrderSettableService()

    def set_result(self, subscription: Subscription):
        self.__subscription_settable.set_result(subscription)

    def generate(self) -> Subscription:
        subscription = self.__subscription_settable.generate()

        promotion = self.__session.query(Promotion)\
            .filter(Promotion.to_quantity == self.__payload.get("month")).first()
        if not promotion:
            raise ServiceParamsException("Invalid promotion")

        price = self.__session.query(Price).join(Plan).filter(Plan.plan_name == self.__payload.get("plan_name")).first()

        if not price:
            raise ServiceParamsException(f"Invalid plan: {price}")

        promotion = self.__session.query(Promotion)\
            .filter(Promotion.to_quantity == self.__payload.get("month")).first()
        if not promotion:
            raise ServiceParamsException(f"Invalid promotion: {promotion}")

        total = int(price.value) * int(self.__payload.get("month")) \
                - int(promotion.to_quantity) / 100 * int(price.value)

        bill = self.__session.query(Bill) \
            .filter(Bill.subscription_id == subscription.id).first()

        if not bill:
            bill = Bill()
            bill.id = generate_uuid()
            bill.sub_total = price.value
            bill.total = total
            bill.discount = promotion.value
            bill.status = 'active'
            bill.subscription_id = subscription.id
            self.__session.add(bill)
            self.__session.add(subscription)

        return subscription
