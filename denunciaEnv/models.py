from django.db import models
import datetime
import json
class Evento(models.Model):
    fecha = models.DateTimeField(auto_now_add = True)
    latitud = models.FloatField(null=True, blank=True, default=None)
    longitud = models.FloatField(null=True, blank=True, default=None)
    descripcion = models.CharField(max_length=1000)
    imagen = models.CharField(max_length=100, default=None)

    def create_JSON(self):
        descripcion_total = "Creado el "+str(self.fecha)+". "+ str(self.descripcion) + "<br> <img src="+ self.imagen +" alt=''  width='300' height='auto'>"
        dic = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            self.longitud,
                            self.latitud
                        ]
                    },
                    "properties": {
                        "title":"",
                        "icon": "monument",
                        "description": descripcion_total 
                    }
                }
        
        return json.dumps( dic)
