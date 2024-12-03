from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Stop, Route
from ..serializers import RouteSerializer, StopSerializer
from ..services.google_maps import GoogleMapsService
from ..services.fare_calculator import FareCalculator

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    google_maps_service = GoogleMapsService()

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

            distance = self.google_maps_service.calculate_distance(origin, destination)
            if not distance:
                return Response(
                    {"error": "Could not calculate distance"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            fare = FareCalculator.calculate_fare(route, distance)
            if not fare:
                return Response(
                    {"error": "No fare rule found for this distance"},
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response({
                "origin": StopSerializer(origin).data,
                "destination": StopSerializer(destination).data,
                "distance": distance,
                "estimated_fare": fare
            })

        except (Stop.DoesNotExist, Route.DoesNotExist) as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND
            )