from paypalpayoutssdk.core import PayPalHttpClient, SandboxEnvironment, LiveEnvironment


def get_paypal_staging_client(client_id, client_secret):
    """Returns PayPal HTTP client instance with environment that has access
    credentials context. Use this instance to invoke PayPal APIs, provided the
    credentials have access.
    """
    environment = SandboxEnvironment(
        client_id=client_id, client_secret=client_secret)
    client = PayPalHttpClient(environment=environment)
    return client


def get_paypal_production_client(client_id, client_secret):
    """Returns PayPal HTTP client instance with environment that has access
        credentials context. Use this instance to invoke PayPal APIs, provided the
        credentials have access.
        """
    environment = LiveEnvironment(
        client_id=client_id, client_secret=client_secret)
    client = PayPalHttpClient(environment=environment)
    return client

