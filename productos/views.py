from .serializers import ProductoSerializer
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Producto
from .filters import ProductoFilter
from django_filters.rest_framework import DjangoFilterBackend

class ListadoProductosView(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductoFilter
    search_fields = ['nombre', 'precio_venta_usd']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Producto.objects.filter(usuario=user)

class AgregarProductoView(CreateAPIView):
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
