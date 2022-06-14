from app.constants import NOT_ALLOW_RESPONSE_CODE
from ._client_exception import ClientException


class ClientMethodNotAllowedException(ClientException):
    __NOT_ALLOW_ERR_MSG = 'Method Not Allowed'

    def get_response_code(self) -> int:
        return NOT_ALLOW_RESPONSE_CODE

    def get_message(self) -> str:
        return self.__NOT_ALLOW_ERR_MSG
