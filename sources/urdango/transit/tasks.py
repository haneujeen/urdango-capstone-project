from urllib.parse import unquote
from django.conf import settings


import requests
from .models import Bus


def get_bus():
    BUS_API_KEY = unquote(settings.BUS_API_KEY)

    url = 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByVehId'

    params = {
        'serviceKey': BUS_API_KEY,
        'vehId': '111033115',  # sample vehicle id
        'resultType': 'json'
    }

    response = requests.get(url, params=params)

    print(response.json())

    return response.json()

st_id = 111000050


def get_test_bus():
    global st_id
    data = {
        "ServiceResult": {
            "comMsgHeader": 0,
            "msgHeader": {
                "headerCd": "0",
                "headerMsg": "정상적으로 처리되었습니다.",
                "itemCount": "0"
            },
            "msgBody": {
                "itemList": {
                    "busType": "1",
                    "congetion": "0",
                    "dataTm": "20190109160221",
                    "isFullFlag": "0",
                    "lastStnId": "111000055",
                    "plainNo": "서울74사2576",
                    "posX": "192126.1048274704",
                    "posY": "457184.85381605756",
                    "stId": str(st_id),  # Update stId with the current value of st_id
                    "stOrd": "1",
                    "stopFlag": "0",
                    "tmX": "126.910807",
                    "tmY": "37.614178",
                    "vehId": "111033115"
                }
            }
        }
    }

    st_id += 1  # Increment st_id

    return data


def update_bus(scheduler):
    print('Fetching bus data')

    data = get_bus()
    data = data['msgBody']['itemList'][0]

    Bus.objects.update_or_create(
        veh_id=data['vehId'],
        defaults={
            'st_id': data['stId'],
            'st_ord': data['stOrd'],
            'stop_flag': data['stopFlag'],
            'data_tm': data['dataTm'],
            'tm_x': data['tmX'],
            'tm_y': data['tmY'],
            'plain_no': data['plainNo'],
            'bus_type': data['busType'],
            'last_stn_id': data['lastStnId'],
            'pos_x': data['posX'],
            'pos_y': data['posY'],
            'passenger_load': data['congetion'],
            'is_full_flag': data['isFullFlag'],
        }
    )

    print(f"Updated bus data for vehId {data['vehId']} stId {data['stId']}")

