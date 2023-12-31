from django.contrib import admin
from . import models
admin.site.site_title = "servicio"
# Register your models here.

@admin.register(models.Servicios)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_filter = ("nombre",)
    search_fields = ("nombre", "descripcion")
    ordering = ("nombre",)
