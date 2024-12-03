from django.db import models
from route.models import Route

class Stop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    route = models.ForeignKey(Route, related_name='stop', on_delete=models.CASCADE)
    stop_order = models.IntegerField()
    wait_time = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Create your models here.
