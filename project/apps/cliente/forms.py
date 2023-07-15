from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre_de_usuario","contraseña","nacimiento", "pais_origen_id"]
