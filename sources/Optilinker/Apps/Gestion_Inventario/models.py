from django.db import models

# Modelo Articulo
class Articulo(models.Model):

    _mostrar_web = ((0, 'No'),(1, 'Si'))
    _estado = ((0, 'Inactivo'),(1, 'Activo'))

    Codigo = models.CharField(max_length=35)
    Nombre = models.CharField(max_length=50, null=True)
    Descripcion = models.CharField(max_length=250)
    Fecha_Creacion = models.DateField(auto_now=True)
    Mostrar_Web = models.BooleanField(default=False)
    Estado = models.BooleanField(default=True)
    
    def __str__(self):
       return self.Codigo

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

# Modelo Transaccion Tipo
class TransaccionTipo(models.Model):

    Nombre = models.CharField(max_length=50, null=True, blank=True)
    Descripcion = models.CharField(max_length=250)
    Fecha_Creacion = models.DateField(auto_now=True)
    Estado = models.CharField(max_length=1, default='1')

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.Nombre)

    class Meta:
        verbose_name = "Tipo de Transacción"
        verbose_name_plural = "Tipos de Transacción"

# Modelo Transaccion
class Transaccion(models.Model):

    Articulo = models.ForeignKey(Articulo, null=False, blank=False, on_delete=models.CASCADE)
    TransaccionTipo = models.ForeignKey(TransaccionTipo, null=False, blank=False, on_delete=models.CASCADE)
    Fecha_Transaccion = models.DateField()
    Fecha_Creacion = models.DateField(auto_now=True)
    Saldo_Actual = models.IntegerField(default=0)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.Articulo)

    class Meta:
        verbose_name = "Transacción"
        verbose_name_plural = "Transacciones"
