from typing import List, Union, Dict

from app.constants import *

from app.constants import SUCCESS_RESPONSE_CODE
from app.models import BaseModel


def response(response_body: dict, response_status: int = SUCCESS_RESPONSE_CODE):
    return response_body, response_status


def response_error(error_message: str, error_code: int) -> tuple:
    return response({
        'message': error_message,
        'code': error_code
    }, error_code)


def response_not_found() -> tuple:
    return response_error('Not found', NOT_FOUND_RESPONSE_CODE)


def response_items(items: List[Union[BaseModel, Dict]],
                   page=None, limit=None, total=None,
                   embedded: list = None,
                   req_serialize=True,
                   excluded: dict = None,
                   included: dict = None,
                   response_status: int = 200,
                   extra_meta: dict = None) -> tuple:
    if req_serialize:
        items = [item.serialize(relations=embedded, excludes=excluded, includes=included) for item in items]

    meta = {}
    if page:
        meta['page'] = page
    if limit:
        meta['limit'] = limit
    if extra_meta:
        meta.update(extra_meta)

    meta['total'] = total or 0
    return response({
        '_items': items,
        '_meta': meta
    }, response_status)
