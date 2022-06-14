from .resources import *

routes = [
    {
        'uri': 'orders',
        'view': OrderResource,
        'methods': ['GET', 'POST', 'PATCH']
    }
]
