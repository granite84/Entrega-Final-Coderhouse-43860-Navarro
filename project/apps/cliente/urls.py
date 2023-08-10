from . import views
from django.urls import path

from .views import crear_cliente, home

app_name = "cliente"

urlpatterns = [
    path("", home, name="home"),
    path('crear/', crear_cliente, name="crear"),
    
    path("cliente/list/", views.ClienteList.as_view(),
         name="cliente_list"),
    path("cliente/create/", views.ClienteCreate.as_view(),
         name="cliente_create"),
    path("cliente/detail/<int:pk>", views.ClienteDetail.as_view(),
         name="cliente_detail"),
    path("cliente/update/<int:pk>", views.ClienteUpdate.as_view(),
         name="cliente_update"),
    path("cliente/delete/<int:pk>", views.ClienteDelete.as_view(),
         name="cliente_delete"),
]
