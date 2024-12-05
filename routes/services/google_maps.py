import googlemaps
from django.conf import settings
from googlemaps.exceptions import ApiError

class GoogleMapsService:
    def __init__(self):
        self.client = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    def calculate_distance(self, origin, destination):
        try:
            result = self.client.distance_matrix(
                origins=f"{origin.latitude},{origin.longitude}",
                destinations=f"{destination.latitude},{destination.longitude}",
                mode="driving"
            )
            
            # Check if the API returned valid data
            if result['rows'][0]['elements'][0]['status'] == 'OK':
                return result['rows'][0]['elements'][0]['distance']['value'] / 1000  # Convert to km
            else:
                return None
        except ApiError as e:
            # Handle API errors such as rate limits or unavailable services
            return {"error": f"Google Maps API error: {str(e)}"}
        except Exception as e:
            # Catch any other exceptions
            return {"error": f"An unexpected error occurred: {str(e)}"}

    def find_nearby_places(self, latitude, longitude, radius=1000):
        try:
            result = self.client.places_nearby(
                location=(latitude, longitude),
                radius=radius
            )
            return result.get('results', [])
        except ApiError as e:
            # Handle API errors
            return {"error": f"Google Maps API error: {str(e)}"}
        except Exception as e:
            # Catch any other exceptions
            return {"error": f"An unexpected error occurred: {str(e)}"}