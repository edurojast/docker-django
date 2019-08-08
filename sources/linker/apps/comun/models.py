from django.db import models

# Region


class Region(models.Model):
    Nombre = models.CharField(max_length=150)
    Fecha_Creacion = models.DateField(auto_now=True)
    Estado = models.BooleanField(default=True)

    def __unicode__(self):
        return self.Nombre

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.Nombre)

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"

# Comuna


class Comuna(models.Model):
    Nombre = models.CharField(max_length=150)
    Region = models.ForeignKey(
        Region, null=False, blank=False, on_delete=models.CASCADE)
    Fecha_Creacion = models.DateField(auto_now=True)
    Estado = models.BooleanField(default=True)

    def __unicode__(self):
        return self.Nombre

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.Nombre)

    class Meta:
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"
