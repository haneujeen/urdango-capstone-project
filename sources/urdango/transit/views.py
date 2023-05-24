from django.shortcuts import render
from .models import SubwayStation


# Create your views here.
def subway_stations(request):
    stations = SubwayStation.objects.all()
    return render(request, 'transit/subway_stations.html', {'stations': stations})
