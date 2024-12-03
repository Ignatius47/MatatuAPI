from rest_framework import serializers
from .models import Matatu

class MatatuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matatu
        fields = ['id', 'driver_name', 'plate_number', 'route', 'capacity', 'status']
