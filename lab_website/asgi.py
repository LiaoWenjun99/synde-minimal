# lab_website/asgi.py

import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat_model.routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab_website.settings")
django.setup()

# Set up routing for both HTTP and WebSocket
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # existing Django views
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)  # ← enables /ws/logs/
    ),
})
