from django.contrib import admin
from linker.apps.inventario.models import *

# registramos las clases
@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('Codigo', 'Nombre', 'Descripcion', 'Fecha_Creacion', 'Estado')
    ordering = ('Codigo',)
    search_fields = ('Codigo', 'Nombre')

# modelos de la aplicación
admin.site.register(TransaccionTipo)
admin.site.register(Transaccion)