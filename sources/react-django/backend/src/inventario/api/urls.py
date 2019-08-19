from django.urls import path
from .views import ArticuloListView, ArticuloDetalleView

urlpatterns = [
    path('', ArticuloListView.as_view()),
    path('<pk>', ArticuloDetalleView.as_view())
]
