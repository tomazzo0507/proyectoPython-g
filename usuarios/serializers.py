# usuarios>serializers.py# Importa el módulo serializers de Django REST framework, utilizado para convertir modelos en formatos como JSON.
from rest_framework import serializers

# Importa el modelo 'usuarios' desde el archivo models.py del mismo directorio.
from .models import usuarios

# Define una clase de serializador llamada 'UsuarioSerializer' que hereda de ModelSerializer.
class UsuarioSerializer(serializers.ModelSerializer):
    # Clase interna Meta que especifica detalles del modelo a serializar.
    class Meta:
        # Especifica que el modelo a usar es 'usuarios'.
        model = usuarios
        # Define los campos del modelo que se incluirán en la serialización.
        fields = ['id', 'nombre', 'correo', 'rol', 'contrasena']
