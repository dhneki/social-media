## chat/routing.py
from django.urls import re_path

from . import consumers
websocket_urlpatterns = [
    re_path(r'notification/(?P<notified>\w+)/$', consumers.NotificationConsumer.as_asgi()),
]
