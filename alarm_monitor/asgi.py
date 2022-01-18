"""
ASGI config for alarm_monitor project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter

from alarm.ws_routing import ws_url_patterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alarm_monitor.settings')

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(ws_url_patterns)),
    'http': get_asgi_application(),
})
