import googlemaps
from django.conf import settings

class GoogleMapsService:
    def __init__(self):
        self.client = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    def calculate_distance(self, origin, destination):
        result = self.client.distance_matrix(
            origins=f"{origin.latitude},{origin.longitude}",
            destinations=f"{destination.latitude},{destination.longitude}",
            mode="driving"
        )
        
        if result['rows'][0]['elements'][0]['status'] == 'OK':
            return result['rows'][0]['elements'][0]['distance']['value'] / 1000  # Convert to km
        return None

    def find_nearby_places(self, latitude, longitude, radius=1000):
        return self.client.places_nearby(
            location=(latitude, longitude),
            radius=radius
        )