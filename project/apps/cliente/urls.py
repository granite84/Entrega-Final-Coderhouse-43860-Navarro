from django.urls import path

from .views import crear_cliente, home

app_name = "cliente"

urlpatterns = [
    path("", home, name="home"),
    path('crear/', crear_cliente, name="crear"),
]
