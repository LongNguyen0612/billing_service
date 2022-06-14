import copy

from flask import request
from marshmallow import Schema, INCLUDE
from marshmallow.schema import SchemaMeta

from ._base_request import BaseRequest


class BaseSchema(Schema):
    class Meta:
        unknown = INCLUDE

    def __init__(self, *args, **kwargs):
        super(BaseSchema, self).__init__(*args, **kwargs)
        self.__init_args = args
        self.__init_kwargs = kwargs


class BaseSchemaRequest(BaseRequest, BaseSchema, metaclass=SchemaMeta):
    def __init__(self, authentication: dict = None, with_init: bool = False, *args, **kwargs):
        BaseRequest.__init__(self, authentication)
        BaseSchema.__init__(self, *args, **kwargs)
        # create schema and validate input request data
        self.__schema = self._create_schema()
        if with_init:
            self.__init_request_data()

    def _create_schema(self) -> Schema:
        """
        Return marshmallow schema that used to validate raw data
        :return:
        """
        return copy.copy(self)

    @staticmethod
    def __load_header() -> dict:
        """
        Return HTTP request's header as dict
        :return:  header dict
        """
        return request.headers

    @staticmethod
    def __load_method() -> str:
        """
        Return HTTP request's method
        :return: method str
        """
        return request.method

    def _fill_data(self) -> dict:
        """
        Validate and return HTTP request's data as dictionary
        :return: dict
        """
        raw_data = self._get_raw_data()
        deserialized_data = self.__schema.load(raw_data)
        deserialized_data = self.__schema.dump(deserialized_data)
        return deserialized_data

    def _get_raw_data(self) -> dict:
        """
        Return HTTP request's unvalidated data as dictionary.
        :return: dict
        """
        return {}

    def _set_schema(self, schema: Schema):
        self.__schema = schema

    def __init_request_data(self):
        self._set_data(self._fill_data(), self.__load_header(), self.__load_method())

    @staticmethod
    def get_url_parameter(key: str):
        """
        Get URL parameter
        :param key: URL parameter's name
        :return: None if key in not included. Otherwise, return string
        """
        return request.args.get(key)

    @staticmethod
    def get_url_list_parameter(key: str) -> list:
        """
        Get array URL parameter
        :param key: array URL parameter's name
        :return:
        """
        return request.args.getlist('{}[]'.format(key))
