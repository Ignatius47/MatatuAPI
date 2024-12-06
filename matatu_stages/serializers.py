from rest_framework import serializers
from .models import Matatu_Stages


class Matatu_Stages_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Matatu_Stages
        fields = '__all__'