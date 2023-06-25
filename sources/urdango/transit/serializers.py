from rest_framework import serializers
from .models import Bus

class BusDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'  # or list the fields you want to include
