from flask import request
from marshmallow import fields, Schema

from ._base_schema_request import BaseSchemaRequest
from logging import getLogger
from app.exceptions import ClientBadRequestException

log = getLogger(__name__)


class BaseModifiedRequest(BaseSchemaRequest):
    def _get_raw_data(self) -> dict:
        try:
            raw_data = {**request.args}
            request_json = request.get_json()
        except Exception as e:
            log.debug('Json body exception: %s', e)
            raise ClientBadRequestException('Invalid json payload')

        if isinstance(request_json, list):
            raw_data.update({'multitude': request_json})
            schema = self._create_schema()

            class NestedList(Schema):
                multitude = fields.List(fields.Nested(schema.__class__))

            self._set_schema(NestedList())
        elif isinstance(request_json, dict):
            raw_data.update(request_json)
        return raw_data
