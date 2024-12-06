from django.db import models
from route.models import Route
from fare.models import Fare
from matatu.models import Matatu
from stop.models import Stop

class Matatu_Stages(models.Model):
    stage_name = models.CharField(max_length=20)
    matatu = models.ForeignKey(Matatu, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    fare = models.ForeignKey(Fare, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)


    def __str__(self):
        return self.stage_name

# Create your models here.
