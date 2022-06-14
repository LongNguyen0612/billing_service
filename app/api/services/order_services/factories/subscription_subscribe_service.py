from app.common import GeneratedException
from app.exceptions import ServiceParamsException
from ..oder_settable import OrderSettableBillService, OrderGenerateService
from ..oder_settable.order_gettable import OrderGettableService
from ..order_generator import SubscriptionGenerator
from sqlalchemy.orm import Session
from app.models import Price, Plan


class SubscriptionSubscribeService:
    def __init__(self, plan_name: str, month: str,
                 account_id: str, order_id: str, session: Session):
        self.__plan_name = plan_name
        self.__account_id = account_id
        self.__order_id = order_id
        self.__month = month
        self.__session = session
        self.__subscription_generator = SubscriptionGenerator()

    def execute(self):
        price = self.__session.query(Price).join(Plan).filter(Plan.plan_name == self.__plan_name).first()

        if not price:
            raise ServiceParamsException("Invalid Price")

        # payload = {
        #     "account_id": self.__account_id,
        #     "order_id": self.__order_id,
        #     "amount": price,
        # }
        # resp = request(method=POST, json=payload, url=ACCOUNT_SERVICE_URL)
        # resp_paid_result = resp.json()
        resp_paid_result = {
                "account_id": self.__account_id,
                "month": self.__month,
                "plan_name": self.__plan_name,
                "order_id": self.__order_id
            }
        order_gettable = OrderGettableService(resp_paid_result, self.__session)
        order_settable = OrderGenerateService(resp_paid_result, self.__session)
        order_settable_bill = OrderSettableBillService(resp_paid_result, self.__session)

        self.__subscription_generator.append_generated(order_gettable)
        self.__subscription_generator.append_generated(order_settable)
        self.__subscription_generator.append_generated(order_settable_bill)

        try:
            return self.__subscription_generator.generate()
        except GeneratedException as e:
            raise ServiceParamsException(str(e))
