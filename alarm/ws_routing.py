from django.urls import path
from .ws_consumers import NotificationWebsocketConsumer

ws_url_patterns = [
    path('ws/notifications/', NotificationWebsocketConsumer.as_asgi())
]
