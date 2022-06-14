from app.api import routes
from app.api.factory import AppFactory
from app.config import BILLING_APP_HOST, BILLING_APP_PORT

factory = AppFactory(routes=routes)
app = factory.create_app()

if __name__ == '__main__':
    app.run(host=BILLING_APP_HOST, port=BILLING_APP_PORT)
