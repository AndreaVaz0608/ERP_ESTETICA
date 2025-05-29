from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    duracao_minutos = models.PositiveIntegerField(help_text="Duração do serviço em minutos")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
