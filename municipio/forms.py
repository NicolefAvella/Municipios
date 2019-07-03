from django import forms
from .models import Municipio, Region

class MunicipioForm(forms.ModelForm):

    class Meta:
        model = Municipio
        fields = ('codigo_m','nombre_m', 'estado','regiones')

class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = ('codigo_r','nombre_r')
