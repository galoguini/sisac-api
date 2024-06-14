from rest_framework import serializers
from .models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Empresa
        fields = [
            'nombre_empresa', 'nombre_fantasia', 'categoria_fiscal', 'tipo_cuenta', 'cuit', 
            'nro_ingresos_brutos', 'fecha_inicio_actividad', 'pais', 'direccion', 'provincia', 
            'localidad', 'telefono', 'email', 'CBU', 'logo'
        ]

    def get_logo(self, obj):
        request = self.context.get('request')
        if obj.logo:
            return request.build_absolute_uri(obj.logo.url)
        return None
