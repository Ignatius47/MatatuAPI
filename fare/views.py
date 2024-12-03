from django.shortcuts import render
from .models import Fare
from rest_framework import viewsets
from .serializers import FareSerializer


class FareViewSet(viewsets.ModelViewSet):
    queryset = Fare.objects.all()
    serializer_class = FareSerializer

# Create your views here.
