from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
<<<<<<< HEAD
    nombre_de_usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=20)
=======
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
>>>>>>> 7a03c1ecfc53cb433e13b2a44ff426a47b481712
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"