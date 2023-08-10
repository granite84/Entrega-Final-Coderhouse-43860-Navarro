from django import forms

from .models import Profesionista


class ProfesionistaForm(forms.ModelForm):
    class Meta:
        model = Profesionista
        fields = ["nombre" ,"apellido","celular","profesion" ,"pais_origen_id", "avatar"]

       