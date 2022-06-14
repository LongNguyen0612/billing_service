from app.common import (
    SideEffected,
    SideEffectedService,
    PostgresSessionCreator)
from app.config import (
    BILLING_APP_DEBUG,
    BILLING_API_DEBUG)
from .resource import Resource


class SessionResource(Resource, SideEffected):
    def __init__(self):
        super(SessionResource, self).__init__()
        self.__base_service = SideEffectedService(debug=BILLING_APP_DEBUG and BILLING_API_DEBUG)
        self.session = PostgresSessionCreator(self).session

    def add_side_effected(self, service):
        self.__base_service.add_side_effected(service)

    def _handle_logic(self, request_method: str, identities, *args, **kwargs):
        return self.__base_service.execute(super(SessionResource, self)._handle_logic, request_method, identities,
                                           *args, **kwargs)
