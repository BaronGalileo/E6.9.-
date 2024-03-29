"""
ASGI config for messanger project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from messanger_chat import routing
from messanger_chat.middleware import JwtAuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messanger.settings')
# django.setup()


# application = get_asgi_application()

application = ProtocolTypeRouter({
   "http": get_asgi_application(),
   'websocket': JwtAuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})

