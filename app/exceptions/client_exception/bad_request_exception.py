from app.constants import BAD_REQUEST_RESPONSE_CODE
from ._client_exception import ClientException


class ClientBadRequestException(ClientException):
    __BAD_REQUEST_ERR_MSG = 'Bad request'

    def get_response_code(self) -> int:
        return BAD_REQUEST_RESPONSE_CODE

    def get_message(self) -> str:
        return self.__BAD_REQUEST_ERR_MSG
