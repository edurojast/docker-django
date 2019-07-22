from django import forms

class ArticuloForm(forms.Form):
    BOOLEAN_CHOICES = (('1', 'True label'), ('0', 'False label'))
    Estado = forms.ChoiceField(choices = BOOLEAN_CHOICES, widget = forms.RadioSelect)