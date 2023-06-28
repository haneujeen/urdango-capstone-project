from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/target_bus/(?P<veh_id>\w+)/(?P<bus_route_id>\w+)/$', consumers.TargetBusConsumer.as_asgi()),
]
