from abc import abstractmethod


class Request:
    @abstractmethod
    def all(self, *args, **kwargs):
        """
        Get all data
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def get(self, keyword, *args, **kwargs):
        """
        Get data with specific keyword
        :param keyword: keyword to get data
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def header(self, name='', *args, **kwargs):
        """
        Get headers
        :param name:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def method(self, *args, **kwargs):
        """
        Get method
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def get_authentication(self,*args, **kwargs):
        """
        Get decoded authentication
        :param args:
        :param kwargs:
        :return:
        """
        pass
