from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from Optilinker.Apps.Gestion_Inventario.models import *
from django.contrib import admin 
from django import forms

# registramos las clases
@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('Codigo', 'Nombre', 'Descripcion', 'Fecha_Creacion', 'Estado')
    ordering = ('Codigo',)
    search_fields = ('Codigo', 'Nombre')

# modelos de la aplicación
admin.site.register(TransaccionTipo)
admin.site.register(Transaccion)