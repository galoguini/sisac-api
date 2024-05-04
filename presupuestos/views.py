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
        usuario = Usuario.objects.get(user_ptr_id=self.request.user.id)
        return Presupuesto.objects.filter(usuario=usuario, empresa=usuario.empresa_seleccionada)

class AgregarPresupuestoView(generics.CreateAPIView):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        usuario = Usuario.objects.get(user_ptr_id=self.request.user.id)
        serializer.save(usuario=usuario)

class EditarPresupuestoView(generics.UpdateAPIView):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]