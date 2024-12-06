from django.contrib import admin
from .models import Matatu_Stages

class MatatuStagesAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'matatu', 'route', 'fare', 'stop')
    search_fields = ('stage_name', 'matatu__name', 'route__name', 'stop__name')
    list_filter = ('route', 'stop')
    ordering = ('stage_name',)

    def matatu_name(self, obj):
        return obj.matatu.name
    matatu_name.short_description = 'Matatu Name'


admin.site.register(Matatu_Stages, MatatuStagesAdmin)

# Register your models here.
