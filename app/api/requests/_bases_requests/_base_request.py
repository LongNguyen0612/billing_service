from ._request import Request


class BaseRequest(Request):
    def __init__(self, authentication: dict):
        self.__data = {}
        self.__header = {}
        self.__method = None
        self.__authentication = authentication

    def all(self, *args, **kwargs) -> dict:
        """
        Get all HTTP request data as dict
        :param args:
        :param kwargs:
        :return:
        """
        return self.__data

    def get(self, keyword, *args, **kwargs):
        """
        Get request data by keyword
        :param keyword:
        :param args:
        :param kwargs:
        :return:
        """
        return self.__data.get(keyword, None)

    def header(self, name='', *args, **kwargs):
        """
        Get all headers or header with name
        :param name:
        :param args:
        :param kwargs:
        :return:
        """
        if len(name) > 0:
            return self.__header.get(name, None)
        return self.__header

    def method(self, *args, **kwargs):
        """
        Get HTTP method
        :param args:
        :param kwargs:
        :return:
        """
        return self.__method

    def _set_data(self, data: dict, header: dict, method):
        self.__data = data
        self.__header = header
        self.__method = method

    def get_authentication(self, key: str = None, *args, **kwargs):
        if key:
            return self.__authentication.get(key)
        return self.__authentication

    def is_admin(self) -> bool:
        return self.get_authentication('is_admin')
