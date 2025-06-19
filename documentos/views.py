from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Documento
from .serializers import DocumentoSerializer

import pandas as pd
from faker import Faker
import random
from datetime import datetime

fake = Faker()

# Vista genérica para listar y crear documentos
class DocumentoListCreateView(generics.ListCreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        
        # Usamos pandas para procesar datos de los documentos
        documentos = Documento.objects.all().values()
        df = pd.DataFrame(documentos)

        if not df.empty:
            resumen = {
                "total_documentos": len(df),
                "disposiciones_comunes": df['disposicion'].value_counts().to_dict(),
                "documentos_por_direccion": df['direccion'].value_counts().to_dict()
            }
        else:
            resumen = {}

        response.data = {
            "documentos": response.data,
            "resumen_pandas": resumen
        }
        return response


# Vista genérica para obtener, actualizar o eliminar un documento
class DocumentoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


# Nueva vista para generar datos falsos con Faker
class GenerarDocumentosFalsosView(APIView):
    def post(self, request):
        for _ in range(10):  # Genera 10 documentos de ejemplo
            Documento.objects.create(
                asunto=fake.sentence(),
                codigo=random.randint(1000, 9999),
                direccion=fake.street_name(),
                disposicion=random.choice(['Conservar', 'Eliminar', 'Digitalizar']),
                fecha=fake.date_between(start_date='-2y', end_date='today'),
                nombre=fake.file_name(),
                procedimiento=fake.word(),
                url=fake.url()
            )
        return Response({"mensaje": "10 documentos falsos generados."}, status=status.HTTP_201_CREATED)

