from rest_framework import serializers
from .models import Fare

class FareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fare
        fields = '__all__'
        extra_kwargs = {
            'min_distance': {'required': True},  # Ensure it's validated
        }
    def validate(self, data):
        if 'min_distance' not in data:
            raise serializers.ValidationError({"min_distance": "This field is required."})
        if data['min_distance'] < 0:
            raise serializers.ValidationError({"min_distance": "Minimum distance cannot be negative."})
        return data