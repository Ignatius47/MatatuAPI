from django.contrib import admin
from .models import Matatu

class MatatuAdmin(admin.ModelAdmin):
    list_display = ('driver_name', 'plate_number', 'route', 'capacity', 'status')
    list_filter = ('status', 'route')
    search_fields = ('driver_name', 'plate_number', 'route__name')

admin.site.register(Matatu, MatatuAdmin)


# Register your models here.
