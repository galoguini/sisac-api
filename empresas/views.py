from rest_framework import generics, permissions
from .models import Empresa
from .serializers import EmpresaSerializer

class AgregarEmpresaView(generics.CreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class ListarEmpresasView(generics.ListAPIView):
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Empresa.objects.filter(usuario=self.request.user)