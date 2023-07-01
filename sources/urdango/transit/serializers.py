from rest_framework import serializers
from .models import Bus

class BusDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'  # or list the fields you want to include


from .models import PushSubscription

class PushSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushSubscription
        fields = ['endpoint', 'p256dh', 'auth']
