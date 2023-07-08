from django.conf import settings
from pywebpush import webpush, WebPushException
import json


class PushService:
    def __init__(self, subscription):
        self.subscription = subscription
        self.private_vapid_key = settings.PRIVATE_VAPID_KEY
        self.public_vapid_key = settings.PUBLIC_VAPID_KEY
        self.payload = None

    def set_subscription(self, subscription):
        self.subscription = subscription

    def set_payload(self, data):
        print("🚀 push_service.py 14: ", json.dumps(data))

        self.payload = {
            "title": f"Updating push for the vehicle {data['vehicle_id']}",
            "body": "Message body",
        }

        print("self.payload = ", self.payload)

    def send_notification(self):
        if self.payload:
            try:
                # Send push notification
                webpush(
                    subscription_info=self.subscription,
                    data=json.dumps(self.payload),
                    vapid_private_key=self.private_vapid_key,
                    vapid_claims={
                        "sub": "mailto:eujeenhan@gmail.com",
                    }
                )

                print("subscription_info = ", self.subscription)
            except WebPushException as e:
                # The subscription was cancelled or the push service rejects the payload for any reason
                print(f"Web push failed: {repr(e)}")
                if e.response and e.response.json():
                    extra = e.response.json()
                    print(f"Remote service replied with a {extra['code']}: {extra['errno']}")
        else:
            print("No payload to send.")