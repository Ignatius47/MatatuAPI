from django.db import models
from route.models import Route

class Matatu(models.Model):
    # Adding choices for the status field
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'In Maintenance'),
    ]

    CAPACiTY_CHOICES = [
        ('14 Seater', '14 Seater'),
        ('33 Seater', '33 Seater'),
        ('52 Seater', '52 Seater'),

    ]
    
    driver_name = models.CharField(max_length=100, blank=False, null=False)
    plate_number = models.CharField(max_length=50, unique=True)  # Ensuring plate number is unique
    route = models.ForeignKey(Route, related_name='matatus', on_delete=models.CASCADE)
    capacity = models.CharField(
        max_length =20,
        choices = CAPACiTY_CHOICES,
        default = '33 Seater',
        blank = False,
        null = False,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',  # Default to 'active' if not set
    )

    def __str__(self):
        return f'{self.driver_name} ({self.plate_number}) - {self.route.name}'

    class Meta:
        verbose_name = "Matatu"
        verbose_name_plural = "Matatus"
