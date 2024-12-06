from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Matatu
from .serializers import MatatuSerializer
from rest_framework import viewsets

class MatatuViewSet(viewsets.ModelViewSet):
    queryset = Matatu.objects.all()
    serializer_class = MatatuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    @action(detail=True, methods=['post'])
    def mark_in_maintenance(self, request, pk=None):
        matatu = self.get_object()
        matatu.status = 'maintenance'
        matatu.save()
        return Response({'status': 'Matatu marked as maintenance'}, status=status.HTTP_200_OK)
