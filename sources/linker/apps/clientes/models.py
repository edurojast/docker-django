from django.conf import settings 
from django.db import models

# Clientes
class Clientes(models.Model):

    Razon_Social = models.CharField(max_length=150)
    Rut = models.CharField(max_length=250)
    Comuna = models.ForeignKey('comun.Comuna', null=False, blank=False, on_delete=models.CASCADE)
    Direccion = models.CharField(max_length=250)
    Telefono_Primario = models.CharField(max_length=20)
    Telefono_Secundario = models.CharField(max_length=20, null=True)
    Encargado_Nombre = models.CharField(max_length=250, null=False)
    Encargado_Correo = models.CharField(max_length=250, null=True)
    Fecha_Creacion = models.DateField(auto_now=True)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return self.Razon_Social

    def __unicode__(self):
        return self.Razon_Social

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

# Historial
class Historial(models.Model):
    TipoContacto = models.ForeignKey('comun.TipoContacto', null=False, blank=False, on_delete=models.CASCADE)
    Fecha_Creacion = models.DateField(auto_now=True)
    Prioridad = models.ForeignKey('comun.Prioridad', null=False, blank=False, on_delete=models.CASCADE)
    Detalle = models.TextField(max_length=500)
    Cliente  = models.ForeignKey(Clientes, null=False, blank=False, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return self.TipoContacto

    def __unicode__(self):
        return self.TipoContacto

    class Meta:
        verbose_name = "Historia"
        verbose_name_plural = "Historial"