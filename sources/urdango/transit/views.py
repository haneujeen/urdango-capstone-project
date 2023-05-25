import requests

from django.shortcuts import render
from django.conf import settings

from .models import SubwayStation
from .forms import RouteForm


# Create your views here.
def subway_stations(request):
    stations = SubwayStation.objects.all()
    return render(request, 'transit/subway_stations.html', {'stations': stations})


# Helper functions below
def get_location_info(location):
    BUS_API_KEY = settings.BUS_API_KEY

    url = 'http://ws.bus.go.kr/api/rest/pathinfo/getLocationInfo'

    params = {
        'serviceKey': BUS_API_KEY,
        'stSrch': location,
        'resultType': 'json'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        import pdb; pdb.set_trace()
        location_info = data['ServiceResult']['msgBody']['itemList'][0]
        return location_info['gpsX'], location_info['gpsY']


def get_subway_path_info(start_x, start_y, end_x, end_y):
    BUS_API_KEY = settings.BUS_API_KEY

    url = 'http://ws.bus.go.kr/api/rest/pathinfo/getPathInfoBySubway'

    params = {
        'serviceKey': BUS_API_KEY,
        'startX': start_x,
        'startY': start_y,
        'endX': end_x,
        'endY': end_y,
        'resultType': 'json'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        path_info = data['ServiceResult']['msgBody']['itemList'][0]
        return path_info


def get_bus_path_info(start_x, start_y, end_x, end_y):
    BUS_API_KEY = settings.BUS_API_KEY

    url = 'http://ws.bus.go.kr/api/rest/pathinfo/getPathInfoByBus'

    params = {
        'serviceKey': BUS_API_KEY,
        'startX': start_x,
        'startY': start_y,
        'endX': end_x,
        'endY': end_y,
        'resultType': 'json'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        path_info = data['ServiceResult']['msgBody']['itemList'][0]
        return path_info


def get_bus_sub_path_info(start_x, start_y, end_x, end_y):
    BUS_API_KEY = settings.BUS_API_KEY

    url = 'http://ws.bus.go.kr/api/rest/pathinfo/getPathInfoByBusNSub'

    params = {
        'serviceKey': BUS_API_KEY,
        'startX': start_x,
        'startY': start_y,
        'endX': end_x,
        'endY': end_y,
        'resultType': 'json'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        path_info = data['ServiceResult']['msgBody']['itemList'][0]
        return path_info


def get_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            start_point = form.cleaned_data['start_point']
            end_point = form.cleaned_data['end_point']
            transportation = form.cleaned_data['transportation']

            start_x, start_y = get_location_info(start_point)
            end_x, end_y = get_location_info(end_point)

            if transportation == 'subway':
                path_info = get_subway_path_info(start_x, start_y, end_x, end_y)
            elif transportation == 'bus':
                path_info = get_bus_path_info(start_x, start_y, end_x, end_y)
            else:
                path_info = get_bus_sub_path_info(start_x, start_y, end_x, end_y)

            return render(request, 'transit/route.html', {'path_info': path_info})
    else:
        form = RouteForm()

    return render(request, 'transit/get_route.html', {'form': form})
