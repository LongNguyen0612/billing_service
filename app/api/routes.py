from app.api.resources import (subscription_routes, plan_routes)

routes = [
    *subscription_routes,
    *plan_routes
]
