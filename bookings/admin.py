from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    #list_display = ['user', 'route', 'stop', 'fare', 'date', 'status']
    list_display = ['user', 'route', 'stop', 'status', 'date']
    list_filter = ['route']
    search_fields= ['route__name', 'status', 'stop__name', 'fare__amount']

admin.site.register(Booking, BookingAdmin)

# Register your models here.
