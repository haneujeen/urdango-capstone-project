from urllib.parse import unquote
from django.conf import settings
import requests
from django.http import JsonResponse
import httpx


async def get_arr_info_by_route_all(rtid):
    url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll'

    params = {
        'serviceKey': unquote('7Sd1p2xp2TxP2FZyZWaNvt%2FjsEW9ULgUgFhwXwMfcTW0vE59yvganCzAwTaCMg7p7todCjZq47xmZ90Av7GC7g%3D%3D'),
        'busRouteId': rtid,
        'resultType': 'json'
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()


async def get_bus_pos_by_veh_id(veh_id):
    url = 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByVehId'

    params = {
        'serviceKey': unquote(settings.BUS_API_KEY),
        'vehId': veh_id,
        'resultType': 'json'
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()


async def get_target_bus(veh_id, bus_route_id):
    try:
        # get bus position by vehicle ID
        response_bus_pos = await get_bus_pos_by_veh_id(veh_id)
        bus_pos_item = response_bus_pos['msgBody']['itemList'][0]

        # get all arrival info by route
        response_route_all = await get_arr_info_by_route_all(bus_route_id)
        route_item_list = response_route_all['msgBody']['itemList']

        # find the index of the station item where 'stId' matches with 'lastStnId' of bus_pos_item
        index, last_station_item = next(
            ((i, item) for i, item in enumerate(route_item_list) if item['stId'] == bus_pos_item['lastStnId']),
            (None, None))

        # if no such item found, raise an exception
        if last_station_item is None:
            raise Exception('No matching current station found')

        # find the stations immediately after and two after the last station
        if index + 1 < len(route_item_list):
            this_station_item = route_item_list[index + 1]
        else:
            raise Exception('No matching next station found')

        if index + 2 < len(route_item_list):
            next_station_item = route_item_list[index + 2]
        else:
            raise Exception('No matching next next station found')

        target_bus = {
            'vehId': bus_pos_item['vehId'],
            'routeId': last_station_item['rtNm'],
            'plainNo': bus_pos_item['plainNo'],
            'lastStnId': bus_pos_item['lastStnId'],
            'lastStnNm': last_station_item['stNm'],
            'this_station_id': this_station_item['stId'], # == last_station_item['nstnId1']
            'this_station_name': this_station_item['stNm'],
            'next_station_id': next_station_item['stId'],
            'next_station_name': next_station_item['stNm'],
            'traTime': this_station_item['traTime1'], # travel time to this_station from last_station (departure)
            'traSpd': this_station_item['traSpd1'],
            'isLast': this_station_item['isLast1'],
        }

        return target_bus

    except Exception as e:
        return {'error': str(e)}


async def update_target_bus(veh_id, bus_route_id):
    # Fetch data from the public API
    data = await get_target_bus(veh_id, bus_route_id)
    print(data)

    return data
