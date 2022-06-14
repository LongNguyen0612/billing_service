from app.exceptions import ClientMethodNotAllowedException


def not_implement(function):
    def method(*args, **kwargs):
        raise ClientMethodNotAllowedException()

    return method
