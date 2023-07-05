from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from urllib.parse import unquote
from django.http import JsonResponse, Http404
from rest_framework import views, status
from .models import PushSubscription, User
from .push_service import PushService
from rest_framework.views import APIView

from django.views.decorators.csrf import csrf_exempt


# Creates a new User object and returns the 'uuid' field to the client
@csrf_exempt
def get_uuid(reqeust):
    user = User.objects.create()
    response = JsonResponse({'uuid': str(user.uuid)})
    response.set_cookie('uuid', str(user.uuid), secure=True, httponly=True)

    return response


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


def get_target_bus(request, veh_id, bus_route_id):
    try:
        # get bus position by vehicle ID
        response_bus_pos = get_bus_pos_by_veh_id(request, veh_id)
        bus_pos_item = response_bus_pos.data['msgBody']['itemList'][0]

        # get all arrival info by route
        response_route_all = get_arr_info_by_route_all(request, bus_route_id)
        route_item_list = response_route_all.data['msgBody']['itemList']

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
            'rtNm': last_station_item['rtNm'],
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

        return JsonResponse(target_bus)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


class PushSubscriptionView(views.APIView):
    def post(self, request, *args, **kwargs):
        print("Requesting!!!", request.data)
        uuid = request.data.get('uuid')
        if not uuid:
            return Response({"detail": "No UUID provided."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(uuid=uuid)
        except User.DoesNotExist:
            return Response({"detail": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)

        subscription = request.data.get('subscription')
        if not subscription:
            return Response({"detail": "No subscription data provided."}, status=status.HTTP_400_BAD_REQUEST)

        # TODO: Validate the subscription data here

        PushSubscription.objects.create(user=user, subscription=subscription)
        print('📦 I received a new push subscription!', subscription)

        welcome_payload = {
            "title": "Subscription created.",
            "body": "Subscription created. The websocket will now be fetching and sending"
                    " the same bus data. Unsubscribing should remove the current subscription object.",
            "icon": "/static/images/icon.png",
            "url": "https://url_for_testing.com"
        }

        push_service = PushService(subscription)
        push_service.payload = welcome_payload
        push_service.send_notification()

        return Response({"detail": "Subscription created."}, status=status.HTTP_201_CREATED)

    def delete(self, request, format=None):
        try:
            user = User.objects.get(uuid=request.uuid)
            subscription = PushSubscription.objects.get(user=user)
        except PushSubscription.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PushMessageView(APIView):
    def post(self, request, format=None):
        # Subscription information would be in the request
        subscription = request.data.get('subscription')
        # Message payload
        message = {"title": "Test Push", "body": "This is a test push message."}
        # Send the push message
        push_service = PushService(subscription, message)
        push_service.send_push()
        return Response(status=202)