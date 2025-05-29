from django.db import models

class Profissional(models.Model):
    ESPECIALIDADES = [
        ('Esteticista', 'Esteticista'),
        ('Massoterapeuta', 'Massoterapeuta'),
        ('Fisioterapeuta', 'Fisioterapeuta'),
        ('Dermatologista', 'Dermatologista'),
        ('Outro', 'Outro'),
    ]
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    especialidade = models.CharField(max_length=30, choices=ESPECIALIDADES)
    comissao_percentual = models.DecimalField(max_digits=5, decimal_places=2, help_text="Percentual da comissão (%)", default=0)
    ativo = models.BooleanField(default=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
