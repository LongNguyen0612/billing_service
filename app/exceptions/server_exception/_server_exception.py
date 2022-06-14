class ServerException(Exception):
    def _create_exception_response_code(self):
        pass

    def _create_exception_message(self):
        pass


class SequenceTerminatedException(Exception):
    pass
