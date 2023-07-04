from django.conf import settings
from pywebpush import webpush, WebPushException
import json


class PushService:
    def __init__(self, subscription, message):
        self.subscription = subscription
        self.message = message
        self.private_vapid_key = settings.PRIVATE_VAPID_KEY
        self.public_vapid_key = settings.PUBLIC_VAPID_KEY

    def send_push(self):
        try:
            # Send push notification
            webpush(
                subscription_info=self.subscription,
                data=json.dumps(self.message),
                vapid_private_key=self.private_vapid_key,
                vapid_claims={
                    "sub": "mailto:eujeenhan@gmail.com",
                }

            )
        except WebPushException as e:
            # The subscription was cancelled or the push service rejects the payload for any reason
            print(f"Web push failed: {repr(e)}")
            if e.response and e.response.json():
                extra = e.response.json()
                print(f"Remote service replied with a {extra['code']}: {extra['errno']}")
