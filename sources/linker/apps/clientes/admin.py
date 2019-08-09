from django.contrib import admin
from linker.apps.clientes.models import *

# modelos de la aplicación
class InLineHistorial(admin.TabularInline):
    model = Historial
    verbose_name = "Contacto"
    verbose_name_plural = "Contactos"


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    inlines = [InLineHistorial]
    list_display = ('Razon_Social', 'Rut', 'getRegion', 'getComuna', 'Telefono_Primario','Encargado_Nombre', 'Encargado_Correo', 'Fecha_Creacion', 'Estado')
    list_editable = ('Estado',)
    list_display_links = ('Razon_Social','Rut')
    ordering = ('Fecha_Creacion',)
    search_fields = ('Razon_Social', 'Rut', 'Comuna__Nombre')
    exclude = ('Usuario')
    

    def getComuna(self, obj):
        return obj.Comuna.Nombre
    getComuna.short_description = 'Comuna'
    getComuna.admin_order_field = 'comuna__nombre'

    def getRegion(self, obj):
        return obj.Comuna.Region.Nombre
    getRegion.short_description = 'Region'
    getRegion.admin_order_field = 'comuna__region__nombre'