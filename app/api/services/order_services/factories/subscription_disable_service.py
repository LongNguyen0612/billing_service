from app.exceptions import ServiceParamsException
from app.models import Subscription, Bill

from sqlalchemy.orm import Session


class SubscriptionDisableService:
    def __init__(self, order_id: str, session: Session):
        self.__order_id = order_id
        self.__session = session

    def execute(self):
        bill = self.__session.query(Bill).join(Subscription).filter(Subscription.order_id == self.__order_id).first()
        if not bill:
            raise ServiceParamsException("Invalid bill")

        bill.status = 'closed'
        bill.subscription.status = 'closed'
        sub_info = {
            "subscription_id": bill.id,
            "bill_id": bill.subscription.id 
        }
        return sub_info