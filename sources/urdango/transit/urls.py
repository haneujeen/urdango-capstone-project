from django.urls import path
from . import views

urlpatterns = [
    path('subway_stations/', views.subway_stations, name='subway_stations'),
    path('get_route/', views.get_route, name='get_route'),
]
