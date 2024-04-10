from django.db import models
from django_countries.fields import CountryField
from usuarios.models import Usuario

# Create your models here.

class Cliente(models.Model):
    IDENTIFICACION = [
    ('CUIL', 'CUIL'),
    ('CUIT', 'CUIT'),
    ('DNI', 'DNI'),
    ('PASAPORTE', 'PASAPORTE'),
    ('OTRO', 'OTRO'),
    ]

    CONDICION = [
    ('RESPONSABLE INSCRIPTO', 'RESPONSABLE INSCRIPTO'),
    ('MONOTRIBUTISTA', 'MONOTRIBUTISTA'),
    ('EXENTO', 'EXENTO'),
    ('EXTERIOR', 'EXTERIOR'),
    ('CONSUMIDOR FINAL', 'CONSUMIDOR FINAL'),
    ('IVA NO ALCANZADO', 'IVA NO ALCANZADO'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_apellido = models.CharField(max_length=100)
    tipo_identificacion = models.CharField(max_length=15, choices=IDENTIFICACION, default='CUIL')
    numero_identificacion = models.CharField(max_length=40)
    otro_identificacion = models.CharField(max_length=40, null=True, blank=True)
    condicion_iva = models.CharField(max_length=30, choices=CONDICION, default='CONSUMIDOR FINAL')
    pais = CountryField()
    provincia = models.CharField(max_length=100, null=True, blank=True)
    localidad = models.CharField(max_length=100, null=True, blank=True)
    domicilio = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=40, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tipo_identificacion} {self.numero_identificacion}"