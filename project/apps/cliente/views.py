from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import ClienteForm

# Create your views here.
from .models import Cliente

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
