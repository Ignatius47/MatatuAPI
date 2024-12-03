from ..models import FareRule

class FareCalculator:
    @staticmethod
    def calculate_fare(route, distance):
        fare_rule = FareRule.objects.filter(
            route=route,
            min_distance__lte=distance,
            max_distance__gte=distance
        ).first()
        
        return fare_rule.fare if fare_rule else None