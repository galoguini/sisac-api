from .serializers import ClienteSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Cliente
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ClienteFilter

class ListadoClientesView(ListAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClienteFilter
    search_fields = ['nombre_apellido', 'numero_identificacion', 'pais', 'provincia', 'localidad', 'email', 'telefono']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cliente.objects.filter(usuario=user)

class AltaClienteView(CreateAPIView):
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)