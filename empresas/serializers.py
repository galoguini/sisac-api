from rest_framework import serializers
from .models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'nombre_empresa', 'nombre_fantasia', 'categoria_fiscal', 'tipo_cuenta', 'cuit', 
            'nro_ingresos_brutos', 'fecha_inicio_actividad', 'direccion', 'provincia', 
            'localidad', 'telefono', 'email', 'CBU'
        ]