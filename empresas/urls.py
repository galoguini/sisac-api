from django.urls import path
from .views import AgregarEmpresaView, ListarEmpresasView

urlpatterns = [
    path('agregar/', AgregarEmpresaView.as_view(), name='agregar-empresa'),
    path('listado/', ListarEmpresasView.as_view(), name='listado-empresas'),
]