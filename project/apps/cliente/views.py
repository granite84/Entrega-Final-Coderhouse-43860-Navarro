from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from . import forms, models

from .forms import ClienteForm
from .models import Cliente
# Create your views here.
def crear_cliente(request):

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:home")
    else:
        form = ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})

def home(request):
    clientes_registros = Cliente.objects.all()
    contexto = {"clientes": clientes_registros}
    return render(request, "cliente/index.html", contexto)

@login_required
def index(request):
    return render(request, "cliente/index.html")

class ClienteList(ListView):
    model = models.Cliente
    
class ClienteCreate(CreateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente:cliente_list")
    
class ClienteDetail(DetailView):
    model = models.Cliente
    
class ClienteUpdate(UpdateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente:cliente_list")
    
class ClienteDelete(DeleteView):
    model = models.Cliente
    success_url = reverse_lazy("cliente:cliente_list")