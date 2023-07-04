from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio
from .tasks import update_target_bus


class TargetBusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.uuid = self.scope['url_route']['kwargs']['uuid']
        self.veh_id = self.scope['url_route']['kwargs']['veh_id']
        self.bus_route_id = self.scope['url_route']['kwargs']['bus_route_id']

        # Start the job for this consumer
        self.job_id = f"{self.uuid}-{self.veh_id}-{self.bus_route_id}"
        self.send_job = asyncio.create_task(self.send_bus())

        await self.accept()

        await self.send(text_data=json.dumps({
            'message': 'Welcome! Connection has been established.',
            'data': 'target_bus'
        }))

    async def disconnect(self, close_code):
        self.send_job.cancel()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'echo': message
        }))

    async def send_bus(self):
        try:
            while True:
                data = await update_target_bus(self.veh_id, self.bus_route_id)

                await self.send(text_data=json.dumps({
                    'message': data
                }))

                await asyncio.sleep(10)  # Wait for 10 seconds before sending the next message
        except asyncio.CancelledError:
            # Handle cancellation
            pass

