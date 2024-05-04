from .serializers import ProductoSerializer
from rest_framework import permissions, generics
from .models import Producto
from .filters import ProductoFilter
from django_filters import rest_framework
from usuarios.models import Usuario

# class ListadoProductosView(generics.ListAPIView):
#     serializer_class = ProductoSerializer
#     filter_backends = [rest_framework.DjangoFilterBackend]
#     filterset_class = ProductoFilter
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         queryset = Producto.objects.filter(usuario=user)
#         filter = ProductoFilter(self.request.GET, queryset=queryset)
#         return filter.qs

class ListadoProductosView(generics.ListAPIView):
    serializer_class = ProductoSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = ProductoFilter
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Producto.objects.filter(usuario=user)

class AgregarProductoView(generics.CreateAPIView):
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        usuario = Usuario.objects.get(user_ptr_id=self.request.user.id)
        serializer.save(usuario=usuario)
