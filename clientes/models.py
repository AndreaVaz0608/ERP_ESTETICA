from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    CATEGORIA_CHOICES = [
        ('starter', 'Starter'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
    ]
    categoria = models.CharField(
        max_length=10,
        choices=CATEGORIA_CHOICES,
        default='starter',
        verbose_name="Categoria"
    )

    def __str__(self):
        return self.nome
