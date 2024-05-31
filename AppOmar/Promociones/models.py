from django.db import models

# Create your models here.
class Promociones(models.Model):
    nombre = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False)