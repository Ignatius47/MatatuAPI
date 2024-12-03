from django.db import models
from route.models import Route
from stop.models import Stop
from fare.models import Fare

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    fare = models.ForeignKey(Fare, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

    
    def __str__(self):
        return f'Booking by {self.user.username} on {self.route.name} from {self.stop.name}'

# Create your models here.
