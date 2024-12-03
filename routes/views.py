from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings
import googlemaps
from .models import Stop, Route, FareRule
from .serializers import StopSerializer, RouteSerializer, FareRuleSerializer

class StopViewSet(viewsets.ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer

    @action(detail=False, methods=['GET'])
    def nearby(self, request):
        lat = request.query_params.get('latitude')
        lng = request.query_params.get('longitude')
        radius = request.query_params.get('radius', 1000)  # Default 1km radius

        if not all([lat, lng]):
            return Response(
                {"error": "Latitude and longitude are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Use Google Maps API to find nearby stops
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
        location = (float(lat), float(lng))
        
        # Query stops within radius
        nearby_stops = Stop.objects.raw(
            """
            SELECT id, name, latitude, longitude,
                   ( 6371 * acos( cos( radians(%s) ) *
                     cos( radians( latitude ) ) *
                     cos( radians( longitude ) - radians(%s) ) +
                     sin( radians(%s) ) *
                     sin( radians( latitude ) )
                   ) ) AS distance
            FROM routes_stop
            HAVING distance < %s
            ORDER BY distance
            """,
            [float(lat), float(lng), float(lat), float(radius) / 1000]
        )

        serializer = self.get_serializer(nearby_stops, many=True)
        return Response(serializer.data)

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    @action(detail=True, methods=['GET'])
    def estimate_fare(self, request, pk=None):
        origin_id = request.query_params.get('origin')
        destination_id = request.query_params.get('destination')

        if not all([origin_id, destination_id]):
            return Response(
                {"error": "Origin and destination stops are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            route = self.get_object()
            origin = Stop.objects.get(id=origin_id)
            destination = Stop.objects.get(id=destination_id)

            # Calculate distance between stops using Google Maps
            gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
            result = gmaps.distance_matrix(
                origins=f"{origin.latitude},{origin.longitude}",
                destinations=f"{destination.latitude},{destination.longitude}",
                mode="driving"
            )

            if result['rows'][0]['elements'][0]['status'] == 'OK':
                distance = result['rows'][0]['elements'][0]['distance']['value'] / 1000  # Convert to km
                
                # Find applicable fare rule
                fare_rule = FareRule.objects.filter(
                    route=route,
                    min_distance__lte=distance,
                    max_distance__gte=distance
                ).first()

                if fare_rule:
                    return Response({
                        "origin": StopSerializer(origin).data,
                        "destination": StopSerializer(destination).data,
                        "distance": distance,
                        "estimated_fare": fare_rule.fare
                    })
                else:
                    return Response({
                        "error": "No fare rule found for this distance"
                    }, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({
                    "error": "Could not calculate distance"
                }, status=status.HTTP_400_BAD_REQUEST)

        except (Stop.DoesNotExist, Route.DoesNotExist) as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND
            )