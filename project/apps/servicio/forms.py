from django import forms

from . import models

class ServicioForm(forms.ModelForm):
    class Meta:
        model = models.ServicioDetalle
        fields = "__all__"
