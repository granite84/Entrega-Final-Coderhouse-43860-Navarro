from django.db import models

# Create your models here.

class Servicios(models.Model):
    nombre = models.CharField(max_length=200, unique=True) 
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    avatar = models.ImageField(upload_to="avatares",blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
