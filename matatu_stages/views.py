from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Matatu_Stages
from .serializers import Matatu_Stages_Serializer


class Matatu_Stages_viewsets(viewsets.ModelViewSet):
    queryset = Matatu_Stages.objects.all()
    serializer_class = Matatu_Stages_Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Create your views here.
