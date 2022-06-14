import json
import re

from flask import request
from marshmallow import fields, ValidationError, validates

from app.constants import DEFAULT_LIMIT
from ._base_schema_request import BaseSchemaRequest


class BaseGetRequest(BaseSchemaRequest):
    id = fields.String(required=False)
    limit = fields.Integer(validate=lambda n: n >= 0, required=False)
    offset = fields.Integer(validate=lambda n: n >= 0, required=False)
    page = fields.Integer(validate=lambda n: n > 0, required=False)
    order = fields.String(validate=lambda order: order in ['asc', 'desc'], required=False)
    sort = fields.String(required=False)
    embedded = fields.List(fields.String(), required=False)
    filters = fields.String(required=False)

    @validates('sort')
    def validate_sort(self, sort):
        if sort not in self.sort_rule():
            raise ValidationError('Invalid sort.')

    @validates('embedded')
    def validate_embedded(self, embedded):
        errors = []
        for key in embedded:
            if key not in self.embedded_keys_rule():
                errors.append('Invalid on embedded key {}.'.format(key))
        if errors:
            raise ValidationError(errors)

    @staticmethod
    def sort_rule() -> list:
        return ['id', '_created', '_updated']

    @staticmethod
    def embedded_keys_rule() -> list:
        return []

    def _get_raw_data(self) -> dict:
        return {
            **request.args,
            'id': self.get_id(),
            'limit': self.get_limit(),
            'offset': self.get_offset(),
            'page': self.get_page(),
            'sort': self.get_sort(),
            'order': self.get_order(),
            'filters': self.get_filters(),
            'embedded': self.get_embedded(),
            **self.filter_rules()
        }

    def get_id(self) -> str:
        """
        Get URL parameter: id.
        :return: Empty string if id is empty or not included.
                Otherwise, return id string.
        """
        return self.get_url_parameter('id') or ''

    def get_limit(self) -> int:
        """
        Get URL parameter: limit.
        :return: 1 if limit is empty, not included or invalid integer format.
                Otherwise, return limit number.
        """
        limit = self.get_url_parameter('limit')
        try:
            return int(limit)
        except (TypeError, ValueError):
            return DEFAULT_LIMIT

    def get_page(self) -> int:
        """
        Get URL parameter: page.
        :return: 1 if page is empty, not included or invalid integer format.
                Otherwise, return page number.
        """
        page = self.get_url_parameter('page')
        try:
            return int(page)
        except (TypeError, ValueError):
            return 1

    def get_offset(self) -> int:
        """
        Get offset number based on limit and page URL parameters.
        :return: Offset number
        """
        page = self.get_page()
        limit = self.get_limit()
        return (page - 1) * limit

    def get_sort(self) -> str:
        """
        Get URL parameter: sort.
        :return: Id if sort is empty, not included or invalid format ([+_][sort_str]).
        Otherwise return sort string.
        """
        sort = self.get_url_parameter('sort')
        if sort:
            match = re.search(r'([-+]?)([_\w]+)', sort)
            sort_str = match.group(2)
            if sort_str:
                return sort_str
        return 'id'

    def get_order(self) -> str:
        """
        Get URL parameter: order.
        :return: Asc if sort is empty, not included or invalid format ([+_][sort_str]).
                 Otherwise return sort string as asc or desc.
        """
        sort = self.get_url_parameter('sort')
        mapping = {
            '+': 'asc',
            '-': 'desc'
        }
        if not sort:
            return mapping['+']
        match = re.search(r'([-+]?)([_\w]+)', sort)
        if not match:
            return mapping['+']
        order_indicator = match.group(1)
        if order_indicator not in mapping:
            return mapping['+']
        return mapping[order_indicator]

    def get_embedded(self) -> set:
        """
        Get URL parameter: embedded.
        :return: Empty list if embedded string is empty, not included or in invalid JSON format.
                 Otherwise, return list embedded relationships
        """
        embedded = []
        url_embedded = self.get_url_parameter('embedded')

        if url_embedded:
            try:
                embedded = json.loads(url_embedded)
            except json.JSONDecodeError:
                raise ValidationError('Invalid embedded')
        return set(embedded)

    def get_filters(self) -> str:
        """
        Get URL parameter: filters.
        :return: Empty string if filter is empty or not included. Otherwise, return filters string.
        """
        filters = self.get_url_parameter('filters')
        if not filters:
            return ''
        return filters

    def filter_rules(self) -> dict:
        """
        Reserve for get_raw_data. The return dict will be merged to input data.
        :return:
        """
        return {}
