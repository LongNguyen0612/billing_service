from app.api.services.order_services._order_generated import OrderSettable
from sqlalchemy.orm import Session

from app.api.services.order_services.oder_settable._order_settable_service import \
    OrderSettableService
from app.exceptions import SequenceTerminatedException, ServiceParamsException
from app.models import Subscription


class OrderGettableService(OrderSettable):
    def __init__(self, payload: dict, session: Session):
        self.__session = session
        self.__payload = payload
        self.__subscription_settable = OrderSettableService()

    def set_result(self, trial: Subscription):
        self.__subscription_settable.set_result(trial)

    def generate(self) -> Subscription:
        try:
            subscription = self.__subscription_settable.generate()
        except SequenceTerminatedException:
            subscription = self.__set_subscription()

        return subscription

    def __set_subscription(self):
        subscription = self.__session.query(Subscription)\
            .filter(Subscription.account_id == self.__payload.get('account_id')).first()

        if subscription:
            raise ServiceParamsException('Subscription existed')

        subscription = Subscription()

        return subscription
