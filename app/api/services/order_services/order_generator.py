from typing import List

from app.common import (Generator, AfterCommit)
from ._order_generated import (OrderAppendableGenerated, OrderSettable, OrderExecutable)
from app.models import Subscription


class SubscriptionGenerator(OrderAppendableGenerated, AfterCommit, OrderExecutable):

    def __init__(self,
                 subscription_settable_services: List[OrderSettable] = None,
                 subscription: Subscription = None):
        self.__generator = Generator(generators=subscription_settable_services,
                                     current_result=subscription)

    def append_generated(self, subscription_settable: OrderSettable, index: int = None):
        self.__generator.append_generated(subscription_settable)

    def set_result(self, subscription: Subscription):
        self.__generator.set_result(subscription)

    def generate(self) -> Subscription:
        return self.__generator.generate()

    def after_commit(self, *args, **kwargs):
        self.__generator.after_commit()

    def execute(self) -> Subscription:
        return self.generate()
