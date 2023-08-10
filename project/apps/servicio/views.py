from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)

from . import forms, models


def index(request):
    return render(request, "servicio/index.html")

class ServiciosList(ListView):
    model = models.Servicios
    
class ServiciosCreate(CreateView):
    model = models.Servicios
    form_class = forms.ServiciosForm
    success_url = reverse_lazy("servicio:servicios_list")
    
class ServiciosDetail(DetailView):
    model = models.Servicios
    
class ServiciosUpdate(UpdateView):
    model = models.Servicios
    form_class = forms.ServiciosForm
    success_url = reverse_lazy("servicio:servicios_list")
    
class ServiciosDelete(DeleteView):
    model = models.Servicios
    success_url = reverse_lazy("servicio:servicios_list")
    
