from django.db import models

# Create your models here.

class ServicioDetalle(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "detalle de servicio"
        verbose_name_plural = "detalles de servicios"
