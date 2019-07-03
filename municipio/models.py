from django.db import models
from .data import TIPO_OPCIONES
from .data import ACTIVO

# Create your models here.
class Region(models.Model):
    codigo_r = models.IntegerField(unique=True)
    nombre_r = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_r


class Municipio(models.Model):
    codigo_m = models.IntegerField(True)
    nombre_m = models.CharField(max_length=200)
    estado = models.CharField(max_length=50, choices=TIPO_OPCIONES, default=ACTIVO)
    #region = models.ForeignKey(Region, on_delete=models.PROTECT)
    regiones = models.ManyToManyField(Region)

    def __str__(self):
        return self.nombre_m

    def get_regiones(self):
        return  self.regiones_set.all() 