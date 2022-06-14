from ._client_exception import ClientException
from ...constants import UNPROCESSABLE_ENTITY_RESPONSE_CODE


class ServiceParamsException(ClientException):
    def get_response_code(self) -> int:
        return UNPROCESSABLE_ENTITY_RESPONSE_CODE

    def get_message(self) -> str:
        return 'Unprocessable entity'
