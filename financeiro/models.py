from django.db import models

class Despesa(models.Model):
    CATEGORIAS = [
        ('FIXA', 'Fixa'),
        ('VARIAVEL', 'Variável'),
        ('ADMIN', 'Administrativa'),
        ('COMISSAO', 'Comissão'),
        ('INSUMO', 'Insumo'),
        ('OUTRA', 'Outra'),
    ]
    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.descricao} - {self.valor:.2f}"
