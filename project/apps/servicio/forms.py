from django import forms

from . import models

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = models.Servicios
        fields = "__all__"
