#documentos>models.py
# Importa el módulo de modelos de Django para definir estructuras de datos.
from django.db import models

# Define el modelo 'Documento', que representa un documento en la base de datos.
class Documento(models.Model):
    # Campo de texto con un máximo de 255 caracteres para el asunto del documento.
    asunto = models.CharField(max_length=255)
    
    # Campo numérico entero para el código del documento.
    codigo = models.IntegerField()
    
    # Campo de texto para la dirección relacionada con el documento.
    direccion = models.CharField(max_length=255)
    
    # Campo de texto para indicar la disposición del documento.
    disposicion = models.CharField(max_length=255)
    
    # Campo de tipo fecha para registrar la fecha del documento.
    fecha = models.DateField()
    
    # Campo de texto con el nombre del documento.
    nombre = models.CharField(max_length=255)
    
    # Campo de texto que indica el procedimiento relacionado al documento.
    procedimiento = models.CharField(max_length=255)
    
    # Campo para almacenar una URL (por ejemplo, enlace a un archivo digital).
    url = models.URLField(max_length=500)

    # Método que define cómo se representará el objeto como cadena de texto.
    def __str__(self):
        return self.nombre
