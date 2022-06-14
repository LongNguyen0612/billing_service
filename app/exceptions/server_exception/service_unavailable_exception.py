from ._server_exception import ServerException
from ...constants import SERVICE_UNAVAILABLE_RESPONSE_CODE


class ServiceUnavailableException(ServerException):
    SERVER_UNAVAILABLE_MSG = 'Service Unavailable'

    def _create_exception_response_code(self) -> int:
        return SERVICE_UNAVAILABLE_RESPONSE_CODE

    def _create_exception_message(self) -> str:
        return self.SERVER_UNAVAILABLE_MSG