from django_filters import rest_framework
from rest_framework import generics, permissions
from .models import Presupuesto
from .serializers import PresupuestoSerializer
from .filters import PresupuestoFilter
from usuarios.models import Usuario

class ListarPresupuestosView(generics.ListAPIView):
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = PresupuestoFilter

    def get_queryset(self):
        user = self.request.user
        return Presupuesto.objects.filter(usuario=user)

class AgregarPresupuestoView(generics.CreateAPIView):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        usuario = self.request.user
        empresa = usuario.empresa_seleccionada
        serializer.save(usuario=usuario, empresa=empresa)

class EditarPresupuestoView(generics.UpdateAPIView):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]

class EliminarPresupuestoView(generics.DestroyAPIView):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'numero_presupuesto'

class DetallePresupuestoView(generics.RetrieveAPIView):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'numero_presupuesto'

class ImpriPresupuestoView(generics.RetrieveAPIView):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'numero_presupuesto'