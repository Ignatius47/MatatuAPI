from django.shortcuts import render
from .models import Fare
from rest_framework import viewsets, serializers, permissions
from .serializers import FareSerializer


class FareViewSet(viewsets.ModelViewSet):
    queryset = Fare.objects.all()
    serializer_class = FareSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        if 'min_distance' not in self.request.data:
            raise serializers.ValidationError({"min_distance": "This field is required."})
        serializer.save()

# Create your views here.
