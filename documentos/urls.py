from django.urls import path
from .views import (
    DocumentoListCreateView,
    DocumentoRetrieveUpdateDestroyView,
    GenerarDocumentosFalsosView
)

urlpatterns = [
    path('documentos/', DocumentoListCreateView.as_view(), name='documento-list-create'),
    path('documentos/<int:pk>/', DocumentoRetrieveUpdateDestroyView.as_view(), name='documento-detail'),
    path('documentos/generar-falsos/', GenerarDocumentosFalsosView.as_view(), name='generar-documentos-falsos'),
]


