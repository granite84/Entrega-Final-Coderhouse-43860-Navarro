from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "servicio"

urlpatterns = [
    path("", views.index, name="home"),
    path("servicios/list/", views.ServiciosList.as_view(),
         name="servicios_list"),
    path("servicios/create/", views.ServiciosCreate.as_view(),
         name="servicios_create"),
    path("servicios/detail/<int:pk>", views.ServiciosDetail.as_view(),
         name="servicios_detail"),
    path("servicios/update/<int:pk>", views.ServiciosUpdate.as_view(),
         name="servicios_update"),
    path("servicios/delete/<int:pk>", views.ServiciosDelete.as_view(),
         name="servicios_delete"),
]
