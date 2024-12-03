from django.contrib import admin
from .models import Fare

class FareAdmin(admin.ModelAdmin):
    list_display = ('route', 'fare_type', 'amount')
    list_filter = ('route',)
    search_fields = ('route__name', 'distance_range')
    list_editable = ('amount',)
    fields = ('route', 'distance_range', 'amount')


admin.site.register(Fare, FareAdmin)
