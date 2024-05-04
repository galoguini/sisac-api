from django.urls import path
from .views import AgregarEmpresaView, ListarEmpresasView, SeleccionarEmpresaView, EditarEmpresaView

urlpatterns = [
    path('agregar/', AgregarEmpresaView.as_view(), name='agregar_empresa'),
    path('listado/', ListarEmpresasView.as_view(), name='listado_empresas'),
    path('seleccionar/', SeleccionarEmpresaView.as_view(), name='seleccionar_empresa'),
    path('editar/', EditarEmpresaView.as_view(), name='editar_empresa'),
]