from django.contrib import admin
from .models import Procedimiento
# Register your models here.

@admin.register(Procedimiento)
class ProcedimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mecanico', 'vehiculo')
    search_fields = ('nombre', 'mecanico__nombre', 'vehiculo__patente')
    list_filter = ('mecanico',)
