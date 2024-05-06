from rest_framework import serializers
from .models import Presupuesto
from clientes.models import Cliente
from productos.models import Producto  

class PresupuestoSerializer(serializers.ModelSerializer):
    cliente = serializers.SlugRelatedField(
        slug_field='nombre_apellido',  
        queryset=Cliente.objects.all(),  
    )
    producto = serializers.SlugRelatedField(  
        slug_field='nombre',  
        queryset=Producto.objects.all(),  
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            self.fields['cliente'].queryset = Cliente.objects.filter(usuario=request.user)
            self.fields['producto'].queryset = Producto.objects.filter(usuario=request.user)

    class Meta:
        model = Presupuesto
        fields = ['id', 'cliente', 'fecha', 'vencimiento', 'moneda','cantidad', 'precio', 'observaciones', 'producto']