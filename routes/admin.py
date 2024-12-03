from django.contrib import admin
from .models import Stop, Route, RouteStop, FareRule

@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'is_major_stop')
    search_fields = ('name',)
    list_filter = ('is_major_stop',)

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_number', 'name', 'base_fare')
    search_fields = ('route_number', 'name')

@admin.register(RouteStop)
class RouteStopAdmin(admin.ModelAdmin):
    list_display = ('route', 'stop', 'stop_order', 'distance_from_start')
    list_filter = ('route',)
    ordering = ('route', 'stop_order')

@admin.register(FareRule)
class FareRuleAdmin(admin.ModelAdmin):
    list_display = ('route', 'min_distance', 'max_distance', 'fare')
    list_filter = ('route',)