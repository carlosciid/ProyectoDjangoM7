from django.db import models

class Propiedad(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
