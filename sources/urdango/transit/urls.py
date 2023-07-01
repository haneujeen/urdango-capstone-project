from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('get_station_by_name/<str:name>/', get_station_by_name, name='get_station_by_name'),
    path('get_station_by_uid/<str:id>/', get_station_by_uid, name='get_station_by_uid'),
    path('get_bus_pos_by_rtid/<str:rtid>/', get_bus_pos_by_rtid, name='get_bus_pos_by_rtid'),
    path('get_arr_info_by_route_all/<str:rtid>/', get_arr_info_by_route_all, name='get_arr_info_by_route_all'),
    path('get_bus_pos_by_veh_id/<str:veh_id>/', get_bus_pos_by_veh_id, name='get_bus_pos_by_veh_id'),
    path('get_target_bus/<str:veh_id>/<str:bus_route_id>/', get_target_bus, name='get_target_bus'),
    path('subscription/', PushSubscriptionView.as_view(), name='subscription'),
    path('push/', PushMessageView.as_view(), name='push')
]
