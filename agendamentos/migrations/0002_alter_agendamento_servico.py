# Generated by Django 5.2.1 on 2025-05-20 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0001_initial'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicos.servico'),
        ),
    ]
