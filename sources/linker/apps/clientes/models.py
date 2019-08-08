from django.db import models

# Clientes


class Clientes(models.Model):

    Razon_Social = models.CharField(max_length=150)
    Rut = models.CharField(max_length=250)
    Comuna = models.ForeignKey('comun.Comuna', null=False, blank=False, on_delete=models.CASCADE)
    Direccion = models.CharField(max_length=250)
    Telefono_Primario = models.CharField(max_length=20)
    Telefono_Secundario = models.CharField(max_length=20,null=False)
    Encargado_Nombre = models.CharField(max_length=250,null=False)
    Encargado_Correo = models.CharField(max_length=250,null=False)
    Fecha_Creacion = models.DateField(auto_now=True)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return self.Comuna.Nombre
    
    def __unicode__(self):
        return self.Razon_Social

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
