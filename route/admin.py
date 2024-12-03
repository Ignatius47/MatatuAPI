from django.contrib import admin
from .models import Route

#@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_location', 'end_location', 'distance', 'estimated_time', 'active')
    list_filter = ('active',)
    search_fields = ('name', 'start_location', 'end_location')
    ordering = ('id',)
    

    def activate_routes(self, request, queryset):
        queryset.update(active=True)
    
    activate_routes.short_description = "Activate selected routes"

    def deactivate_routes(self, request, queryset):
        queryset.update(active=False)
    
    deactivate_routes.short_description = "Deactivate selected routes"

    actions = [activate_routes, deactivate_routes]

admin.site.register(Route, RouteAdmin)
