from django.urls import path
from . import views

urlpatterns = [
    path('subway_stations/', views.subway_stations, name='subway_stations'),
]
