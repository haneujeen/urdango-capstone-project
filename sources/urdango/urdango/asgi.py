"""
ASGI config for urdango project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import re_path

from channels.routing import ProtocolTypeRouter, URLRouter

from transit import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urdango.settings')

application = get_asgi_application()

websocket_urlpatterns = [
    re_path(r'ws/target_bus/(?P<veh_id>\w+)/(?P<bus_route_id>\w+)/$', consumers.TargetBusConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        websocket_urlpatterns
    ),
})
