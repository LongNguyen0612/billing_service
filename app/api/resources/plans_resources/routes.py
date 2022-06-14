from .resources import PlanResource

routes = [
    {
        'uri': 'plans',
        'view': PlanResource,
        'methods': ['GET']
    },
    {
        'uri': 'plans/<id>',
        'view': PlanResource,
        'methods': ['GET']
    }
]
