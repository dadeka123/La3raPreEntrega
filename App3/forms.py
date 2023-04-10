from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre_equipo', 'region', 'fecha_fundacion']
        widgets = {
            'nombre_equipo': forms.TextInput(attrs={'style': 'display: block'}),
            'region': forms.TextInput(attrs={'style': 'display: block'}),
            'fecha_fundacion': forms.DateInput(attrs={'type': 'date', 'style': 'display: block'}),
        }
