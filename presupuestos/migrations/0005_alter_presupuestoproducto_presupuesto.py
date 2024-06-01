# Generated by Django 5.0.3 on 2024-05-28 01:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0004_remove_presupuesto_cantidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuestoproducto',
            name='presupuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='presupuestos.presupuesto'),
        ),
    ]
