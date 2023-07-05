from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio

from django.apps import apps
from .tasks import update_target_bus


class TargetBusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.uuid = self.scope['url_route']['kwargs']['uuid']
        self.veh_id = self.scope['url_route']['kwargs']['veh_id']
        self.bus_route_id = self.scope['url_route']['kwargs']['bus_route_id']

        # Start the job for this consumer
        self.job_id = f"{self.uuid}-{self.veh_id}-{self.bus_route_id}"
        self.send_job = asyncio.create_task(self.send_bus())

        # Fetch and send initial data
        initial_bus = await update_target_bus(self.veh_id, self.bus_route_id)

        await self.accept()

        await self.send(text_data=json.dumps(initial_bus))
        print('Initial data sent')

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
                try:
                    print('Updating target bus')
                    data = await update_target_bus(self.veh_id, self.bus_route_id)
                    if data:
                        await self.send(text_data=json.dumps(data))

                        # delay the model import until Django is fully initialized.
                        User = apps.get_model('transit', 'User')
                        PushSubscription = apps.get_model('transit', 'PushSubscription')

                        # If a subscription exists for this client, send a push notification.
                        user = User.objects.get(uuid=self.uuid)
                        subscription = PushSubscription.objects.get(user=user)
                        if subscription:
                            print("Subscription found")
                    else:
                        print('No data received from update_target_bus')
                    await asyncio.sleep(10)  # Wait for 10 seconds before sending the next message
                except Exception as e:
                    print(f'An error occurred: {e}')
        except asyncio.CancelledError:
            # Handle cancellation
            print('Task was cancelled')



