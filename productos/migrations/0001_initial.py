# Generated by Django 5.0.3 on 2024-06-11 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo_sku', models.CharField(blank=True, max_length=50, null=True)),
                ('codigo_barra', models.CharField(blank=True, max_length=50, null=True)),
                ('categoria', models.CharField(max_length=10)),
                ('tasa_iva', models.CharField(max_length=17)),
                ('unidad_medida', models.CharField(max_length=10)),
                ('precio_venta_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
