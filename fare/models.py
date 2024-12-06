from django.db import models
from  route.models import Route

class Fare(models.Model):
    route = models.ForeignKey(Route, related_name='fares', on_delete=models.CASCADE)
    min_distance = models.FloatField(default=0.0)
    max_distance = models.FloatField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    FARE_CHOICES = [
        ('M-pesa', 'M-pesa'),
        ('Cash', 'Cash'),
        ('Courage', 'Courage'),
        ('Kidney', 'Kidney'),
        ('Fists', 'Fists'),
        ('Sambaza', 'Sambaza'),
        ('Boxing', 'Boxing'),
        ('Wreso', 'Wreso'),
    ]
    
    fare_type = models.CharField(max_length=10, choices=FARE_CHOICES)
    currency = models.CharField(max_length=10, default="KES")

    def __str__(self):
        return f"{self.fare_type} fare for {self.route.name}"


# Create your models here.
