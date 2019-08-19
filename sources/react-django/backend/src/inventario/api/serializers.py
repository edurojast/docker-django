from rest_framework import serializers
from inventario.models import Articulo


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('codigo',)
