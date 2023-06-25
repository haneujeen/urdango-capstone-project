from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusDataViewSet

router = DefaultRouter()
router.register(r'busdata', BusDataViewSet, basename='busdata')

urlpatterns = [
    path('', include(router.urls)),
]
