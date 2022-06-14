from flask import Flask
from flask_cors import CORS
import uuid

from app.config import BILLING_APP_NAME, BILLING_APP_PREFIX, LOG_LEVEL
from app.constants import REQUIRED_ATTRIBUTES, ROUTE_ATTRIBUTES, VIEW_ATTR, URI_ATTR, METHOD_ATTR, ALLOWED_METHODS
from app.log import setup_app_level_logger


class AppFactory(object):
    def __init__(self, app_name: str = None, prefix: str = None, routes: list = None):
        self.app_name = app_name or BILLING_APP_NAME
        self.api_prefix = prefix or BILLING_APP_PREFIX
        self.routes = routes

    def create_app(self, ):
        setup_app_level_logger(name="app", level=LOG_LEVEL)
        app = Flask(self.app_name)
        formatted_routes = self.__create_routes(self.routes)
        self.__add_routes(app, formatted_routes)

        # Setting up CORS
        CORS(app=app,
             supports_credentials=True,
             automatic_options=True)

        return app

    # Configure api
    def __create_routes(self, routes: list) -> list:
        formatted_routes = []
        for route in routes:
            for required_attrs in REQUIRED_ATTRIBUTES:
                if not route.get(required_attrs):
                    continue
            route_item = {}
            for key, default_value in ROUTE_ATTRIBUTES.items():
                route_item[key] = route.get(key, default_value)

            try:
                resource_cls = route_item.get(VIEW_ATTR)
                resource = resource_cls
                route_item[VIEW_ATTR] = resource
                formatted_routes.append(route_item)

                uri = route_item.get(URI_ATTR)
                uri = self.api_prefix + '/{}'.format(uri)
                route_item[URI_ATTR] = uri

            except TypeError:
                pass

        return formatted_routes

    @staticmethod
    def __add_routes(app: Flask, routes: list):
        for route in routes:
            endpoint = route[URI_ATTR]
            resource = route[VIEW_ATTR]
            methods = route.get(METHOD_ATTR, ALLOWED_METHODS)
            app.add_url_rule(endpoint,
                             view_func=resource.get_view(name=str(uuid.uuid4())),
                             methods=methods)
