from django.urls import path
from .views import (
    UsuarioListCreateView,
    UsuarioRetrieveUpdateDestroyView,
    GenerarUsuariosFalsosView
)

urlpatterns = [
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail'),
    path('usuarios/generar-falsos/', GenerarUsuariosFalsosView.as_view(), name='generar-usuarios-falsos'),
]


