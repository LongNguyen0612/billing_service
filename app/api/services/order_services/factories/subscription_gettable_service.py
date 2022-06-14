from app.exceptions import ServiceParamsException
from app.models import Subscription, Bill
from sqlalchemy import inspect
from sqlalchemy.orm import Session


class SubscriptionGettableService:
    def __init__(self, account_id: str, session: Session) -> None:
        self.__account_id = account_id
        self.__session = session

    def execute(self):
        if self.__account_id:
          subscription_account = self.__session.query(Subscription).filter(Subscription.account_id == self.__account_id).all()
          list_subscription = []
          for sub in subscription_account:
            bill = self.__session.query(Bill).filter(Bill.subscription_id == sub.id).all()
            dict_subscription = {
                "subscription": sub,
                "bill": bill
            }  

            list_subscription.append(dict_subscription)
            list_sub_final = []
            for sub in list_subscription:
                sub_object = {}
                sub_object.update(self.__object_as_dict(sub.get("subscription")))
                bill = [self.__object_as_dict(bill_handled) for bill_handled in sub.get("bill")]
                sub_object.update({"bill": bill})
                list_sub_final.append(sub_object)

        return list_sub_final



    @staticmethod
    def __object_as_dict(obj):
        return {c.key: getattr(obj, c.key)
                for c in inspect(obj).mapper.column_attrs}
