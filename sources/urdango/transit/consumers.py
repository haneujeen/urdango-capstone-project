from channels.generic.websocket import AsyncWebsocketConsumer
from .scheduler import scheduler
import json


class TargetBusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.uuid = self.scope['url_route']['kwargs']['uuid']
        self.veh_id = self.scope['url_route']['kwargs']['veh_id']
        self.bus_route_id = self.scope['url_route']['kwargs']['bus_route_id']

        # Start the job for this consumer
        self.job_id = f"{self.uuid}-{self.veh_id}-{self.bus_route_id}"
        scheduler.add_job(self.send_bus, 'interval',
                          seconds=10, id=self.job_id, replace_existing=True)

        await self.accept()

        await self.send(text_data=json.dumps({
            'message': 'Welcome! Connection has been established.',
            'data': 'target_bus'
        }))

    async def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'echo': message
        }))

