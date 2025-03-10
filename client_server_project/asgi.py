"""
ASGI config for client_server_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
#Neccessary libraries for using Socket Programming
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack #built in middleware to simplify backend
import network_app.routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'client_server_project.settings')

#Used in client_server_project.settings to help with backend communications
application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            network_app.routing.websocket_url_patterns
        )
    )
})
