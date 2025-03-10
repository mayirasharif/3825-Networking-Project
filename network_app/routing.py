from django.urls import re_path

from . import consumers

#This is used in helping to route the BackEnd with the ASGI file which is used for SOCKET messaging
websocket_url_patterns = [
    re_path(r'socket-server/', consumers.Consumer.as_asgi())

]