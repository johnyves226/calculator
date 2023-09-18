"""
ASGI config for calculator project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "calculator.settings")

django_asgi_app  = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter  # noqa: E402
from reactpy_django import REACTPY_WEBSOCKET_ROUTE  # noqa: E402
from channels.auth import AuthMiddlewareStack  # noqa: E402
from channels.sessions import SessionMiddlewareStack  # noqa: E402

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": SessionMiddlewareStack(
            AuthMiddlewareStack(
                URLRouter(
                    [REACTPY_WEBSOCKET_ROUTE],
                )
            )
        ),
    }
)
