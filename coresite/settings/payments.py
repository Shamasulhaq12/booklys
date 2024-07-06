from .base import env
from utils.payment_utils import get_paypal_staging_client, get_paypal_production_client

# PayPal Settings Variables
PAYPAL_CLIENT_ID = env('PAYPAL_CLIENT_ID')
PAYPAL_SECRET_KEY = env('PAYPAL_SECRET_KEY')
IS_PRODUCTION = bool(env("IS_PRODUCTION", default=False))

PAYPAL_CLIENT = get_paypal_staging_client(
        client_id=PAYPAL_CLIENT_ID,
        client_secret=PAYPAL_SECRET_KEY)

# PayPal Client Object
if IS_PRODUCTION:
    PAYPAL_CLIENT = get_paypal_production_client(
        client_id=PAYPAL_CLIENT_ID,
        client_secret=PAYPAL_SECRET_KEY
    )