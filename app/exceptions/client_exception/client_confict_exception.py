from app.constants import CONFLICT_RESPONSE_CODE
from ._client_exception import ClientException


class ClientConflictException(ClientException):

    def get_response_code(self) -> int:
        return CONFLICT_RESPONSE_CODE

    def get_message(self) -> str:
        return 'CONFLICT'
