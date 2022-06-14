from app.api.factory import response_items
from app.exceptions import ServiceParamsException
from app.api.resources.session_resource import SessionResource
from app.api.resources.orders_resources.requests import OrderPatchRequest, \
                                                        OrderPostRequest, \
                                                        OrderGetRequest
from app.api.services.order_services.factories import SubscriptionSubscribeService, \
                                                    SubscriptionDisableService, \
                                                    SubscriptionGettableService
import logging
from flask import request as flask_request

logger = logging.getLogger(__name__)


class OrderResource(SessionResource):

    def _get(self, request: OrderGetRequest, *args, **kwargs):
        try:
            account_id = flask_request.args.get("account_id")
            sub_gettable = SubscriptionGettableService(account_id, self.session)
            sub_executed = sub_gettable.execute()
        except ServiceParamsException as exception:
            logger.log("Process failed")

        return response_items(sub_executed,
                              total=len(sub_executed),
                              req_serialize=False)

    def _post(self, request: OrderPostRequest, *args, **kwargs):
        orders = []
        multitude = request.get('multitude') or []
        if not multitude:
            multitude.append(request.all())

        for item in multitude:
            plan_name = item.get('plan_name')
            months = item.get('month')
            account_id = item.get('account_id')
            order_id = item.get('order_id')
            order_factories = SubscriptionSubscribeService(plan_name, months, account_id, order_id, self.session)
            order = order_factories.execute()
            orders.append(order)

        items = [order.serialize() for order in orders]
        return response_items(items, req_serialize=False, total=len(orders))

    def _patch(self, request: OrderPatchRequest):
        multitude = request.get('multitude') or []
        if not multitude:
            multitude.append(request.all())
        disabled_sub = None
        for item in multitude:
            account_id = item.get('order_id')
            order_factories = SubscriptionDisableService(account_id, self.session)
            disabled_sub = order_factories.execute()

        return disabled_sub, 204
