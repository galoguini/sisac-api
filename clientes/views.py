from .serializers import ClienteSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import filters
from .models import Cliente

class ListadoClientesView(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre_apellido', 'numero_identificacion']
    ordering_fields = ['nombre_apellido', 'numero_identificacion']

class AltaClienteView(CreateAPIView):
    serializer_class = ClienteSerializer