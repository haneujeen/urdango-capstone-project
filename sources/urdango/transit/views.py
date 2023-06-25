from rest_framework import viewsets
from .models import Bus
from .serializers import BusDataSerializer

class BusDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusDataSerializer

