from django.contrib import admin
from linker.apps.clientes.models import *

# modelos de la aplicación
@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('Razon_Social', 'Rut', 'getRegion', 'getComuna', 'Direccion', 'Telefono_Primario', 'Telefono_Secundario',
    'Encargado_Nombre', 'Encargado_Correo', 'Fecha_Creacion', 'Estado')
    ordering = ('Fecha_Creacion',)
    search_fields = ('Razon_Social', 'Rut', 'Comuna')

    def getComuna(self, obj):
        return obj.Comuna.Nombre
    getComuna.short_description = 'Comuna'
    getComuna.admin_order_field = 'comuna__nombre'

    def getRegion(self, obj):
        return obj.Comuna.Region.Nombre
    getRegion.short_description = 'Region'
    getRegion.admin_order_field = 'comuna__region__nombre'