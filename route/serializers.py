from rest_framework import serializers
from .models import Route
from fare.serializers import FareSerializer
from stop.serializers import StopSerializer

class RouteSerializer(serializers.ModelSerializer):
    fare = FareSerializer(many=True, read_only=True)
    stops = StopSerializer(many=True, read_only=True)

    
    class Meta:
        model = Route
        fields = '__all__'