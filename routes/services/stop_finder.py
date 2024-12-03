from django.db import connection

class StopFinder:
    @staticmethod
    def find_nearby_stops(latitude, longitude, radius_km):
        with connection.cursor() as cursor:
            cursor.execute("""
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
            """, [float(latitude), float(longitude), float(latitude), radius_km])
            return cursor.fetchall()