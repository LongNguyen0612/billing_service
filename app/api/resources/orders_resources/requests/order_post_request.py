from xml.sax.handler import feature_external_ges
from marshmallow import fields

from app.api.requests import PostRequest


class OrderPostRequest(PostRequest):
    month = fields.String(required=True)
    account_id = fields.String(required=True)
    plan_name = fields.String(required=True)
    order_id = fields.String(required=True)
    started_at = fields.DateTime()

