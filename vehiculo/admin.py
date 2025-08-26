from django.contrib import admin
from .models import Vehículo

# Register your models here.
@admin.register(Vehículo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('patente', 'modelo', 'año', 'dueño')
    search_fields = ('patente', 'modelo', 'dueño')
    list_filter = ('año',)
