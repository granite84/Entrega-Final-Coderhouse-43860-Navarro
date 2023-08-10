from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from . import forms, models

# Create your views here.
from .models import Profesionista
from .forms import ProfesionistaForm
def crear_profesionista(request):

    if request.method == "POST":
        form = ProfesionistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesionista:home")
    else:
        form = ProfesionistaForm()
    return render(request, "profesionista/crear_profesionista.html", {"form": form})

def home(request):
    profesionistas_registros = Profesionista.objects.all()
    contexto = {"profesionistas": profesionistas_registros}
    return render(request, "profesionista/index.html", contexto)


@login_required
def index(request):
    return render(request, "profesionista/index.html")

class ProfesionistaList(ListView):
    model = models.Profesionista
    
class ProfesionistaCreate(CreateView):
    model = models.Profesionista
    form_class = forms.ProfesionistaForm
    success_url = reverse_lazy("profesionista:profesionista_list")
    
class ProfesionistaDetail(DetailView):
    model = models.Profesionista
    
class ProfesionistaUpdate(UpdateView):
    model = models.Profesionista
    form_class = forms.ProfesionistaForm
    success_url = reverse_lazy("profesionista:profesionista_list")
    
class ProfesionistaDelete(DeleteView):
    model = models.Profesionista
    success_url = reverse_lazy("profesionista:profesionista_list")
    
    
    