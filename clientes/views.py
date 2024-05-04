from .serializers import ClienteSerializer
from rest_framework import generics
from .models import Cliente
from rest_framework import permissions
from django_filters import rest_framework
from .filters import ClienteFilter
from usuarios.models import Usuario

class ListadoClientesView(generics.ListAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = ClienteFilter
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cliente.objects.filter(usuario=user)

class AltaClienteView(generics.CreateAPIView):
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        usuario = Usuario.objects.get(user_ptr_id=self.request.user.id)
        serializer.save(usuario=usuario)