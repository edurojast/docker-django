from django.contrib import admin
from linker.apps.clientes.models import *

# modelos de la aplicación
@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('Razon_Social', 'Rut', 'Comuna', 'Direccion', 'Telefono_Primario', 'Telefono_Secundario',
    'Encargado_Nombre', 'Encargado_Correo', 'Fecha_Creacion', 'Estado')
    ordering = ('Fecha_Creacion',)
    search_fields = ('Razon_Social', 'Rut', 'Comuna')