from django.db import models
from mecanico.models import Mecánico
from vehiculo.models import Vehículo

# Create your models here.

class Procedimiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name="Descripción")
    mecanico = models.ForeignKey("mecanico.Mecánico", on_delete=models.CASCADE)
    vehiculo = models.ForeignKey("vehiculo.Vehículo", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.vehiculo.patente})"


