from rest_framework import viewsets
from .models import Bus
from .serializers import BusDataSerializer

class BusDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusDataSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from urllib.parse import unquote

@api_view(['GET'])
def get_station_by_name(request, name):
    url = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByName'
    print(name)

    params = {
        'serviceKey': unquote('GMDNZxLlo35v0mYu1b%2BEExd5aIdZ93RCUBhUBo2w73LWCtz%2Ft%2F%2FKdGfzDVUdcyqljjwvNa5Dtd56uELhovFZRw%3D%3D'),
        'stSrch': name,
        'resultType': 'json'
    }
    response = requests.get(url, params=params)
    return Response(response.json())


@api_view(['GET'])
def get_station_by_uid(request, id):
    url = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid'

    params = {
        'serviceKey': unquote('GMDNZxLlo35v0mYu1b%2BEExd5aIdZ93RCUBhUBo2w73LWCtz%2Ft%2F%2FKdGfzDVUdcyqljjwvNa5Dtd56uELhovFZRw%3D%3D'),
        'arsId': id,
        'resultType': 'json'
    }
    response = requests.get(url, params=params)
    return Response(response.json())

@api_view(['GET'])
def get_bus_pos_by_rtid(request, rtid):
    url = 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid'

    params = {
        'serviceKey': unquote('GMDNZxLlo35v0mYu1b%2BEExd5aIdZ93RCUBhUBo2w73LWCtz%2Ft%2F%2FKdGfzDVUdcyqljjwvNa5Dtd56uELhovFZRw%3D%3D'),
        'busRouteId': rtid,
        'resultType': 'json'
    }
    response = requests.get(url, params=params)
    return Response(response.json())

@api_view(['GET'])
def get_arr_info_by_route_all(reqeust, rtid):
    url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll'

    params = {
        'serviceKey': unquote('7Sd1p2xp2TxP2FZyZWaNvt%2FjsEW9ULgUgFhwXwMfcTW0vE59yvganCzAwTaCMg7p7todCjZq47xmZ90Av7GC7g%3D%3D'),
        'busRouteId': rtid,
        'resultType': 'json'
    }
    response = requests.get(url, params=params)
    return Response(response.json())

@api_view(['GET'])
def get_bus_pos_by_veh_id(reqeust, veh_id):
    url = 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByVehId'

    params = {
        'serviceKey': unquote('GMDNZxLlo35v0mYu1b%2BEExd5aIdZ93RCUBhUBo2w73LWCtz%2Ft%2F%2FKdGfzDVUdcyqljjwvNa5Dtd56uELhovFZRw%3D%3D'),
        'vehId': veh_id,
        'resultType': 'json'
    }
    response = requests.get(url, params=params)
    return Response(response.json())