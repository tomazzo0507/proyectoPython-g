# documentos>serializers.py
# Importa el módulo serializers de Django REST Framework para crear serializadores.
from rest_framework import serializers

# Importa el modelo 'Documento' definido en models.py.
from .models import Documento

# Define un serializador para el modelo 'Documento', basado en ModelSerializer.
class DocumentoSerializer(serializers.ModelSerializer):
    # Clase interna Meta que contiene la configuración del serializador.
    class Meta:
        # Modelo que se va a serializar.
        model = Documento
        # Lista de campos del modelo que se incluirán en la serialización.
        fields = ['id', 'asunto', 'codigo', 'direccion', 'disposicion', 'fecha', 'procedimiento', 'url']
