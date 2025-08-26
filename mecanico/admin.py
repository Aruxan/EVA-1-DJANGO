from django.contrib import admin
from .models import Mecánico


# Register your models here.
@admin.register(Mecánico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'especialidad')
    search_fields = ('nombre', 'especialidad')
    list_filter = ('especialidad',)