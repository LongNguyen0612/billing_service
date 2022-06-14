import logging
from typing import Type
from flask import g
from flask.views import MethodView
from app.api.factory.utils import not_implement
from app.api.factory.utils.response import response
from app.api.requests._bases_requests._base_schema_request import BaseSchemaRequest
from app.constants import BAD_REQUEST_RESPONSE_CODE, INTERNAL_ERROR_RESPONSE_CODE, SUCCESS_RESPONSE_CODE
from app.exceptions import ClientException, ServerException
from marshmallow import ValidationError

from app.models import BaseModel

log = logging.getLogger(__name__)


class Resource:
    # NOTE: Reserved resource methods
    @not_implement
    def _get(self, *args, **kwargs):
        pass

    @not_implement
    def _post(self, *args, **kwargs):
        pass

    @not_implement
    def _patch(self, *args, **kwargs):
        pass

    @not_implement
    def _delete(self, *args, **kwargs):
        pass

    @not_implement
    def _put(self, *args, **kwargs):
        pass

    def handle(self, request_method: str, *args, **kwargs) -> tuple:
        try:
            # NOTE: Init request to validate request payloads
            identities = self._handle_identity()
            return self._handle_logic(request_method, identities, *args, **kwargs)

        except (ServerException, ClientException) as application_exception:
            log.info(application_exception)
            return self._handle_response(application_exception.get_message(),
                                         application_exception.get_response_code())
        except ValidationError as validated_exception:
            return self._handle_response(str(validated_exception), BAD_REQUEST_RESPONSE_CODE)

        except Exception as exception:
            log.exception(exception)
            return self._handle_response('Internal Server Error', INTERNAL_ERROR_RESPONSE_CODE)

    @classmethod
    def get_view(cls, name: str, method_view: type(MethodView) = None):
        if method_view:
            view = method_view
        else:
            view = ResourceMethodView
        return view.as_view(resource=cls, name=name)

    @staticmethod
    def _handle_identity():
        return {}

    def _handle_logic(self, request_method: str, identities, *args, **kwargs):
        method_to_call = getattr(self, '_{}'.format(request_method))
        request_param_name, request = self.__initial_request(method_to_call, authentication=identities)
        if request_param_name:
            kwargs[request_param_name] = request
        return method_to_call(*args, **kwargs)

    @staticmethod
    def _handle_response(message: str, response_code: int = SUCCESS_RESPONSE_CODE):
        return response(response_body={'code': response_code, 'message': message}, response_status=response_code)

    @staticmethod
    def __initial_request(method_to_call, authentication):
        type_hints = method_to_call.__annotations__
        for parameter_name, type_hint in type_hints.items():
            if issubclass(type_hint, BaseSchemaRequest):
                request_type = type_hint
                return parameter_name, request_type(authentication, True)
        return None, None


class ResourceMethodView(MethodView):
    def __init__(self, *args, **kwargs):
        self.resource_cls = kwargs.pop('resource')

    def get(self, *args, **kwargs):
        return self._handle_with_resource('get', *args, **kwargs)

    def post(self, *args, **kwargs):
        return self._handle_with_resource('post', *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self._handle_with_resource('patch', *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self._handle_with_resource('delete', *args, **kwargs)

    def put(self, *args, **kwargs):
        return self._handle_with_resource('put', *args, **kwargs)

    def _handle_with_resource(self, method: str, *args, **kwargs):
        resource = self.resource_cls()
        resource_response = resource.handle(method, *args, **kwargs)
        return resource_response
