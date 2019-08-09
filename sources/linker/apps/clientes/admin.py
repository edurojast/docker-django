from django.contrib import admin
from linker.apps.clientes.models import *

# modelos de la aplicación
class InLineContactos(admin.TabularInline):
    model = Contactos
    extra = 1
    max_num = 3


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    inlines = [InLineContactos]
    list_display = ('Razon_Social', 'Rut', 'getRegion', 'getComuna', 'Direccion', 'Telefono_Primario', 'Telefono_Secundario',
    'Encargado_Nombre', 'Encargado_Correo', 'Fecha_Creacion', 'Estado')
    #list_editable = ('Estado',)
    list_display_links = ('Razon_Social','Rut')
    ordering = ('Fecha_Creacion',)
    search_fields = ('Razon_Social', 'Rut', 'Comuna__Nombre')

    def getComuna(self, obj):
        return obj.Comuna.Nombre
    getComuna.short_description = 'Comuna'
    getComuna.admin_order_field = 'comuna__nombre'

    def getRegion(self, obj):
        return obj.Comuna.Region.Nombre
    getRegion.short_description = 'Region'
    getRegion.admin_order_field = 'comuna__region__nombre'