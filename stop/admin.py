from django.contrib import admin
from .models import Stop

#@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'route', 'stop_order', 'wait_time')
    list_filter = ('route',)
    search_fields = ('name', 'location', 'route__name')
    ordering = ('route', 'stop_order')


admin.site.register(Stop, StopAdmin)