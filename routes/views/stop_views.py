from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Stop
from ..serializers import StopSerializer
from ..services.stop_finder import StopFinder

class StopViewSet(viewsets.ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer

    @action(detail=False, methods=['GET'])
    def nearby(self, request):
        lat = request.query_params.get('latitude')
        lng = request.query_params.get('longitude')
        radius = float(request.query_params.get('radius', 1000))  # Default 1km radius

        if not all([lat, lng]):
            return Response(
                {"error": "Latitude and longitude are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        nearby_stops = StopFinder.find_nearby_stops(
            latitude=float(lat),
            longitude=float(lng),
            radius_km=radius / 1000
        )
        
        stops = [Stop.objects.get(id=stop[0]) for stop in nearby_stops]
        serializer = self.get_serializer(stops, many=True)
        return Response(serializer.data)