from abc import (ABC, abstractmethod)

from app.common import (Generated, SettableGenerated, GeneratedAppendable, Executable)
from app.models import Subscription


class OrderGenerated(Generated, ABC):

    @abstractmethod
    def generate(self) -> Subscription:
        pass


class OrderSettable(OrderGenerated, SettableGenerated, ABC):

    @abstractmethod
    def set_result(self, subscription: Subscription):
        pass


class OrderGeneratedAppendable(GeneratedAppendable, ABC):

    @abstractmethod
    def append_generated(self, order_settable: OrderSettable, index: int = None):
        pass


class OrderAppendableGenerated(OrderGeneratedAppendable, OrderSettable, ABC):
    pass


class OrderExecutable(Executable, ABC):
    @abstractmethod
    def execute(self) -> Subscription:
        pass
