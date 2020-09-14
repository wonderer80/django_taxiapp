from rest_framework import serializers
from .models import Dispatch

class DispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch
        fields = ('id', 'passenger_id', 'driver_id', 'address', 'assigned_at', 'created_at', 'updated_at',)
        read_only_fields = ('created_at',)