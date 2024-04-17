from rest_framework import generics, permissions, response, views, status
from .models import Empresa
from .serializers import EmpresaSerializer
from usuarios.models import Usuario

class AgregarEmpresaView(generics.CreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        usuario = Usuario.objects.get(user_ptr_id=self.request.user.id)
        serializer.save(usuario=usuario)

class ListarEmpresasView(generics.ListAPIView):
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Empresa.objects.filter(usuario=self.request.user)
    
class SeleccionarEmpresaView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        empresa_id = request.data.get('empresa_id')
        try:
            empresa = Empresa.objects.get(id=empresa_id, usuario=request.user)
            request.user.empresa_seleccionada = empresa
            request.user.save()
            return response.Response(status=status.HTTP_200_OK)
        except Empresa.DoesNotExist:
            return response.Response({'error': 'Empresa no encontrada.'}, status=status.HTTP_404_NOT_FOUND)