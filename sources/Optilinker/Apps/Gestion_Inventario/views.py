from django.shortcuts import render
from django.views.generic.edit import UpdateView
from Gestion_Inventario.models import *
from django import forms

class ArticuloForm(forms.ModelForm):
    boolfield = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'False'), (True, 'True')),
                   widget=forms.RadioSelect
                )

    class Meta:
         model = Articulo