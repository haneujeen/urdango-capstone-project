from rest_framework import serializers
from .models import PushSubscription


class PushSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushSubscription
        fields = ['pk', 'endpoint', 'expiration_time', 'p256dh', 'auth']