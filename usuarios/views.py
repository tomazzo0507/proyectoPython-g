from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import usuarios
from .serializers import UsuarioSerializer

import pandas as pd
from faker import Faker
import random

fake = Faker()

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = usuarios.objects.all()
    serializer_class = UsuarioSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        # Procesamiento con Pandas
        data = usuarios.objects.all().values()
        df = pd.DataFrame(data)

        if not df.empty:
            resumen = {
                "total_usuarios": len(df),
                "roles_comunes": df['rol'].value_counts().to_dict()
            }
        else:
            resumen = {}

        response.data = {
            "usuarios": response.data,
            "resumen_pandas": resumen
        }
        return response


class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = usuarios.objects.all()
    serializer_class = UsuarioSerializer


class GenerarUsuariosFalsosView(APIView):
    def post(self, request):
        for _ in range(10):
            usuarios.objects.create(
                nombre=fake.name(),
                correo=fake.email(),
                rol=random.choice(['Admin', 'Editor', 'Usuario']),
                contrasena=fake.password(length=10)
            )
        return Response({"mensaje": "10 usuarios falsos generados."}, status=status.HTTP_201_CREATED)

