from app.api.services.order_services._order_generated import OrderSettable

from app.exceptions import SequenceTerminatedException
from app.models import Subscription


class OrderSettableService(OrderSettable):
    def __init__(self):
        self.__subscriptions = None

    def set_result(self, subscription: Subscription):
        self.__subscriptions = subscription

    def generate(self) -> Subscription:
        if not self.__subscriptions:
            raise SequenceTerminatedException()

        return self.__subscriptions
