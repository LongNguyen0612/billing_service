from marshmallow import fields

from app.api.requests import PatchRequest


class OrderPatchRequest(PatchRequest):
    order_id = fields.String(required=True)
