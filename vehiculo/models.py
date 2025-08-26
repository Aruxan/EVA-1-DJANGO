from django.db import models

# Create your models here.
class Vehículo(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    dueño = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patente} - {self.modelo}"