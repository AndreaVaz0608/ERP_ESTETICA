# clientes/utils.py

from datetime import date
from .models import Cliente

def aniversariantes_hoje():
    hoje = date.today()
    return Cliente.objects.filter(
        data_nascimento__month=hoje.month,
        data_nascimento__day=hoje.day
    )
