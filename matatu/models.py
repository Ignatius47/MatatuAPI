from django.db import models

class Stop(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField(blank=True)
    is_major_stop = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Route(models.Model):
    route_number = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    stops = models.ManyToManyField(Stop, through='RouteStop')
    base_fare = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Route {self.route_number} - {self.name}"

class RouteStop(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    stop_order = models.PositiveIntegerField()
    distance_from_start = models.DecimalField(max_digits=8, decimal_places=2)  # in kilometers

    class Meta:
        ordering = ['stop_order']

    def __str__(self):
        return f"{self.route} - Stop {self.stop_order}: {self.stop}"

class FareRule(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    min_distance = models.DecimalField(max_digits=8, decimal_places=2)
    max_distance = models.DecimalField(max_digits=8, decimal_places=2)
    fare = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.route} - {self.min_distance}km to {self.max_distance}km: KES {self.fare}"
    

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    fare = models.ForeignKey(FareRule, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True) 

    
    def __str__(self):
        return f'Booking by {self.user.username} on {self.route.name} from {self.stop.name}'