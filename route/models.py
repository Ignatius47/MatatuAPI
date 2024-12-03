from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=100)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    distance = models.FloatField()
    estimated_time = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Create your models here.
