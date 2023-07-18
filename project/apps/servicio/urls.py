from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "servicio"

urlpatterns = [
    path("", views.index, name="home"),
    path("servicio/list/", views.ServicioDetalleList.as_view(),
         name="serviciodetalle_list"),
    path("servicio/create/", views.ServicioDetalleCreate.as_view(),
         name="serviciodetalle_create"),
    path("servicio/detail/<int:pk>", views.ServicioDetalleDetail.as_view(),
         name="serviciodetalle_detail"),
    path("servicio/update/<int:pk>", views.ServicioDetalleUpdate.as_view(),
         name="serviciodetalle_update"),
    path("servicio/delete/<int:pk>", views.ServicioDetalleDelete.as_view(),
         name="serviciodetalle_delete"),
]
