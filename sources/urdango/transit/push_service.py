from django.conf import settings
from pywebpush import webpush, WebPushException
from py_vapid import Vapid
import json

class PushService:
    def __init__(self, subscription, message):
        self.subscription = subscription
        self.message = message
        self.private_vapid_key = settings.PRIVATE_VAPID_KEY
        self.public_vapid_key = settings.PUBLIC_VAPID_KEY

    def _get_vapid_headers(self):
        # Create a Vapid object with private key
        vapid = Vapid.from_string(self.private_vapid_key)

        # Define the Vapid claims (subject)
        claims = {
            'aud': '/'.join(self.subscription["endpoint"].split('/')[0:3]),
            'sub': 'mailto:eujeenhan@gmail.com'
        }

        # Return the signed Vapid headers
        return vapid.sign(claims)

    def send_push(self):
        # Get the Vapid headers
        vapid_headers = self._get_vapid_headers()

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
