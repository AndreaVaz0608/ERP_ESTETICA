# Generated by Django 5.2.1 on 2025-05-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campanhas', '0001_initial'),
        ('clientes', '0002_cliente_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensagemagendada',
            name='destinatarios',
            field=models.ManyToManyField(blank=True, to='clientes.cliente'),
        ),
    ]
