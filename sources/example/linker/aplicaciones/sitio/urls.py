from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name="acceso"),
    path('escritorio/', views.escritorioView, name="escritorio")
]
