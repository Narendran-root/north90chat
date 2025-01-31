import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from chat.consumers import ChatConsumer  # Make sure this import is correct

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatapp.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/chat/<str:username>/", ChatConsumer.as_asgi()),
        ])
    ),
})
