"""Production settings for Credentials"""


def plugin_settings(settings):
    # Credentials Settings
    settings.CREDENTIALS_INTERNAL_SERVICE_URL = settings.get(
        'CREDENTIALS_INTERNAL_SERVICE_URL', settings.CREDENTIALS_INTERNAL_SERVICE_URL
    )
    settings.CREDENTIALS_PUBLIC_SERVICE_URL = settings.get(
        'CREDENTIALS_PUBLIC_SERVICE_URL', settings.CREDENTIALS_PUBLIC_SERVICE_URL
    )
