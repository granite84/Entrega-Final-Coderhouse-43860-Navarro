from . import views
from django.urls import path

from .views import crear_profesionista, home

app_name = "profesionista"

urlpatterns = [
    path("", home, name="home"),
    path('crear_profesionista/', crear_profesionista, name="crear_profesionista"),
    path("", views.index, name="home"),
    
    path("profesionista/list/", views.ProfesionistaList.as_view(),
         name="profesionista_list"),
    path("profesionista/create/", views.ProfesionistaCreate.as_view(),
         name="profesionista_create"),
    path("profesionista/detail/<int:pk>", views.ProfesionistaDetail.as_view(),
         name="profesionista_detail"),
    path("profesionista/update/<int:pk>", views.ProfesionistaUpdate.as_view(),
         name="profesionista_update"),
    path("profesionista/delete/<int:pk>", views.ProfesionistaDelete.as_view(),
         name="profesionista_delete"),
]


