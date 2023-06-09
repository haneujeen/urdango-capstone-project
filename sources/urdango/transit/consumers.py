from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio

from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

from .tasks import update_target_bus
from .push_service import PushService


class TargetBusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.uuid = self.scope['url_route']['kwargs']['uuid']
        self.veh_id = self.scope['url_route']['kwargs']['veh_id']
        self.bus_route_id = self.scope['url_route']['kwargs']['bus_route_id']

        await self.accept()

        # Create a PushService instance
        self.push_service = PushService({})

        # Start the job for this consumer
        self.job_id = f"{self.uuid}-{self.veh_id}-{self.bus_route_id}"
        self.send_job = asyncio.create_task(self.send_bus())
        print("WebSocket task created")

        # Fetch and send initial data
        initial_bus = await update_target_bus(self.veh_id, self.bus_route_id)

        await self.send(text_data=json.dumps(initial_bus))
        print('Initial data sent')

    async def disconnect(self, close_code):
        self.send_job.cancel()
        # Delete the User and its associated PushSubscription
        await self.delete_user_and_subscription()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'echo': message
        }))

    @sync_to_async
    def get_subscription(self):
        User = apps.get_model('transit', 'User')
        PushSubscription = apps.get_model('transit', 'PushSubscription')

        user = User.objects.get(uuid=self.uuid)
        subscription = PushSubscription.objects.get(user=user)

        # Set the subscription in the PushService
        self.push_service.set_subscription(subscription.subscription)
        print("Subscription set to push service")

        return user, subscription

    async def send_bus(self):
        try:
            while True:
                try:
                    # Update the target bus data,
                    print('Updating target bus')
                    data = await update_target_bus(self.veh_id, self.bus_route_id)

                    # If there's valid data, 1. send it to the WebSocket connection
                    # and 2. send a push message with the data
                    if data:
                        # 1.1. Socket simply sends the data to the client
                        await self.send(text_data=json.dumps(data))
                        # 2.1. Check for the push notification subscription
                        try:
                            await self.get_subscription()
                            # 2.2. Update the payload in the PushService
                            self.push_service.set_payload(data)
                            # 2.3. Send the notification
                            print('Sending push notification')
                            self.push_service.send_notification()

                        except ObjectDoesNotExist:
                            print("No subscription found or this is an unsubscribed user")
                            pass
                    else:
                        print('No data received from update_target_bus')
                    await asyncio.sleep(10)  # Wait for 10 seconds before sending the next message

                except Exception as e:
                    print(f'An error occurred: {e}')
                    break
        except asyncio.CancelledError:
            # Handle cancellation
            print('Task was cancelled')

    @sync_to_async
    def delete_user_and_subscription(self):
        User = apps.get_model('transit', 'User')
        PushSubscription = apps.get_model('transit', 'PushSubscription')

        try:
            user = User.objects.get(uuid=self.uuid)
            PushSubscription.objects.filter(user=user).delete()
            user.delete()
            print("User and associated PushSubscription deleted")
        except ObjectDoesNotExist:
            print("User or PushSubscription does not exist")

