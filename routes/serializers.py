from rest_framework import serializers
from .models import Stop, Route, RouteStop, FareRule

class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ['id', 'name', 'latitude', 'longitude', 'description', 'is_major_stop']

class RouteStopSerializer(serializers.ModelSerializer):
    stop = StopSerializer()

    class Meta:
        model = RouteStop
        fields = ['stop', 'stop_order', 'distance_from_start']

class RouteSerializer(serializers.ModelSerializer):
    stops = RouteStopSerializer(source='routestop_set', many=True, read_only=True)

    class Meta:
        model = Route
        fields = ['id', 'route_number', 'name', 'description', 'base_fare', 'stops']

class FareRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FareRule
        fields = ['id', 'route', 'min_distance', 'max_distance', 'fare']