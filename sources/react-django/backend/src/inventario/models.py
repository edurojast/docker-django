from django.db import models


class Articulo(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.codigo
