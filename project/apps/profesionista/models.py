from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profesionista(models.Model):
    nombre = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profesional" )
    apellido = models.CharField(max_length= 50)
    celular = models.CharField(max_length=50)
    profesion = models.ForeignKey("servicio.Servicios", on_delete=models.CASCADE, null = False)
    pais_origen_id = models.ForeignKey("cliente.Pais", on_delete=models.SET_NULL, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatares",blank=True, null=True)
    
    def __str__(self):
        return self.nombre.username, self.avatar
    
  