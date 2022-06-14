import os

BILLING_APP_NAME = os.getenv('BILLING_APP_NAME', 'app')
BILLING_APP_HOST = os.getenv('BILLING_HOST', '0.0.0.0')
BILLING_APP_PORT = os.getenv('BILLING_API_PORT', 8082)
BILLING_APP_PREFIX = os.getenv('PREFIX', '/api/v1')
BILLING_BROADCAST_PREFIX = os.getenv('BILLING_BROADCAST_PREFIX', 'api_v4')
BILLING_APP_DEBUG = bool(int(os.getenv('BILLING_APP_DEBUG', 0)))
BILLING_API_DEBUG = bool(int(os.getenv('BILLING_API_DEBUG', 0)))
BILLING_CONSUMER_DEBUG = bool(int(os.getenv('BILLING_CONSUMER_DEBUG', 0)))

POSTGRES_URL = os.getenv('POSTGRES_URL', 'postgresql://postgres:nhatlong6122@10.5.8.162:5432/billing_service')

REDIS_URL = os.getenv('REDIS_URI', None)

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
