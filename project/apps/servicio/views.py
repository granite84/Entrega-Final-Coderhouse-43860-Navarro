from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)

from . import forms, models

@login_required
def index(request):
    return render(request, "servicio/index.html")

class ServicioDetalleList(ListView):
    model = models.ServicioDetalle
    
class ServicioDetalleCreate(CreateView):
    model = models.ServicioDetalle
    form_class = forms.ServicioForm
    success_url = reverse_lazy("servicio:serviciodetalle_list")
    
class ServicioDetalleDetail(DetailView):
    model = models.ServicioDetalle
    
class ServicioDetalleUpdate(UpdateView):
    model = models.ServicioDetalle
    form_class = forms.ServicioForm
    success_url = reverse_lazy("servicio:serviciodetalle_list")
    
class ServicioDetalleDelete(DeleteView):
    model = models.ServicioDetalle
    success_url = reverse_lazy("servicio:serviciodetalle_list")
    
    
    