from django.contrib import admin
from .models import Fare


class FareAdmin(admin.ModelAdmin):
    list_display = ('route', 'fare_type', 'amount', 'min_distance', 'max_distance', 'currency')
    list_filter = ('route', 'fare_type', 'currency')
    search_fields = ('route__name', 'fare_type')
    list_editable = ('amount',)
    fields = ('route', 'fare_type', 'min_distance', 'max_distance', 'amount', 'currency')
    ordering = ('route', 'min_distance')


admin.site.register(Fare, FareAdmin)
