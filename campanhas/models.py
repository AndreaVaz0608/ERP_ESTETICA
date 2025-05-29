# app/models.py

from django.db import models
from django.contrib.auth import get_user_model
from clientes.models import Cliente

class MensagemAgendada(models.Model):
    TIPO_MENSAGEM_CHOICES = [
        ('aniversario', 'Aniversário'),
        ('lembrete', 'Lembrete de Agendamento'),
        ('promocional', 'Promoção'),
        ('comemorativa', 'Data Comemorativa'),
        ('personalizada', 'Personalizada'),
    ]

    titulo = models.CharField(max_length=120)
    tipo = models.CharField(max_length=20, choices=TIPO_MENSAGEM_CHOICES)
    data_disparo = models.DateTimeField(null=True, blank=True)
    mensagem = models.TextField()
    destinatarios = models.ManyToManyField(Cliente, blank=True)
    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_display()})"

