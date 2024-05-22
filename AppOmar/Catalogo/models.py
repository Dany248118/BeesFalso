from django.db import models

class Productos (models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    retornable = models.BooleanField(default=False)
    tamaño_embalaje = models.PositiveIntegerField(default=1)
    existencias = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', default='productos/default.jpeg')

    def __str__(self):
        return self.marca, self.categoria