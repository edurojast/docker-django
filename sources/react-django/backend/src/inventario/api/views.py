from rest_framework.generics import ListAPIView, RetrieveAPIView
from inventario.models import Articulo
from .serializers import ArticuloSerializer


class ArticuloListView(ListAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer


class ArticuloDetalleView(RetrieveAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
