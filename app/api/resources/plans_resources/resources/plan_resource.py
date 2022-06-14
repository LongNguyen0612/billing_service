from app.api.factory import response_not_found, response_items
from app.api.resources.session_resource import SessionResource
from app.api.services.plan_services.plan_service import PlanService
from app.exceptions import ServiceParamsException
from ..requests import PlanGetRequest
from flask import request as flask_request
import logging

logger = logging.getLogger(__name__)


class PlanResource(SessionResource):

    def _get(self, request: PlanGetRequest, *args, **kwargs):
        try:
            month = flask_request.args.get("month")
            model_id = kwargs.get("id") or request.get("id")
            plan = PlanService(self.session, month, model_id)
            plan_executed = plan.execute()

        except ServiceParamsException as e:
            logger.info("Invalid plan with model because of %s", e)
            return response_not_found()

        return response_items(plan_executed,
                              total=len(plan_executed),
                              req_serialize=False)
