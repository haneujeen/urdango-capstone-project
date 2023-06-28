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


import requests
from django.http import JsonResponse, Http404

def get_target_bus(request, veh_id, bus_route_id):
    try:
        response_bus_pos = get_bus_pos_by_veh_id(request, veh_id)
        print(response_bus_pos.data)
        bus_pos_item = response_bus_pos.data['msgBody']['itemList'][0]

        response_route_all = get_arr_info_by_route_all(request, bus_route_id)
        route_item = next(
            (i for i in response_route_all.data['msgBody']['itemList'] if i['vehId1'] == bus_pos_item['vehId']),
            None)
        if not route_item:
            raise Http404('No matching next station found')

        # fetch the station name
        response_stn_name = get_arr_info_by_route_all(request, bus_route_id)
        stn_name_items = response_stn_name.data['msgBody']['itemList']
        last_stn_nm_item = next((i for i in stn_name_items if i['stId'] == bus_pos_item['lastStnId']), None)
        nstn_nm_item = next((i for i in stn_name_items if i['stId'] == route_item['nstnId1']), None)
        if not last_stn_nm_item or not nstn_nm_item:
            raise Http404('No matching station name found')

        target_bus = {
            'vehId': bus_pos_item['vehId'],
            'rtNm': route_item['rtNm'],
            'plainNo': bus_pos_item['plainNo'],
            'lastStnId': bus_pos_item['lastStnId'],
            'lastStnNm': last_stn_nm_item['stNm'],
            'nstnId': route_item['nstnId1'],
            'nstnNm': nstn_nm_item['stNm'],
            'traTime': route_item['traTime1'],
            'traSpd': route_item['traSpd1'],
            'isLast': route_item['isLast1'],
        }

        return JsonResponse(target_bus)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)