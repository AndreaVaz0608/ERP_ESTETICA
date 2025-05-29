from django.db import models
from clientes.models import Cliente
from servicos.models import Servico

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servico)  # Agora permite múltiplos serviços
    data_hora = models.DateTimeField()
    profissional = models.CharField(max_length=100, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    confirmado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        nomes_servicos = ", ".join(s.nome for s in self.servicos.all())
        return f"{self.cliente.nome} - {self.data_hora.strftime('%d/%m/%Y %H:%M')} - {nomes_servicos}"
