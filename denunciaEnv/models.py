from django.db import models
import datetime
class Evento(models.Model):
    fecha = models.DateTimeField(auto_now_add = True)
    latitud = models.FloatField(null=True, blank=True, default=None)
    longitud = models.FloatField(null=True, blank=True, default=None)
    descripcion = models.CharField(max_length=1000)
    imagen = models.CharField(max_length=100)


