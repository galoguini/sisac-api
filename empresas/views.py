from rest_framework import generics, permissions, response, views, status, exceptions
from .models import Empresa
from .serializers import EmpresaSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError

class ListarEmpresasView(generics.RetrieveAPIView):
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Empresa.objects.get(usuario=self.request.user)
        except Empresa.DoesNotExist:
            raise exceptions.NotFound("No se encontró la empresa para el usuario actual.")
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class EditarEmpresaView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        empresa = Empresa.objects.get(usuario=request.user)
        serializer = EmpresaSerializer(empresa)
        return Response(serializer.data)

    def put(self, request):
        empresa = Empresa.objects.get(usuario=request.user)
        serializer = EmpresaSerializer(empresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        empresa = Empresa.objects.get(usuario=request.user)
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AgregarEmpresaView(generics.CreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if Empresa.objects.filter(usuario=self.request.user).exists():
            raise ValidationError('Este usuario ya tiene una empresa.')

        logo_file = self.request.FILES.get('logo')
        if logo_file:
            serializer.validated_data['logo'] = logo_file

        serializer.save(usuario=self.request.user)

class SeleccionarEmpresaView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            empresa = Empresa.objects.get(usuario=request.user)
            request.user.empresa_seleccionada = empresa
            request.user.save()
            return response.Response(status=status.HTTP_200_OK)
        except Empresa.DoesNotExist:
            return response.Response({'error': 'Empresa no encontrada.'}, status=status.HTTP_404_NOT_FOUND)