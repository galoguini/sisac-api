from django.urls import path
from .views import AgregarEmpresaView, ListarEmpresasView

urlpatterns = [
    path('agregar/', AgregarEmpresaView.as_view(), name='agregar_empresa'),
    path('listado/', ListarEmpresasView.as_view(), name='listado_empresas'),
]