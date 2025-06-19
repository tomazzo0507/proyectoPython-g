from django.db import models

class usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    rol = models.CharField(max_length=50)  # Agregado max_length
    contrasena = models.CharField(max_length=128)  # Agregado max_length

    def __str__(self):
        return self.nombre  # Muestra el nombre en lugar de usar super()

