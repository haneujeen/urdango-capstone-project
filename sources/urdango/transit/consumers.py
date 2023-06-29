from channels.generic.websocket import AsyncWebsocketConsumer
import json


class TargetBusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.veh_id = self.scope['url_route']['kwargs']['veh_id']
        self.bus_route_id = self.scope['url_route']['kwargs']['bus_route_id']

        # fetch initial target bus data

        await self.accept()

        await self.send(text_data=json.dumps({
            'message': 'Welcome! Connection has been established.'
        }))

    async def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

