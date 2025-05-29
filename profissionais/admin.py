from django.contrib import admin
from .models import Profissional

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade', 'comissao_percentual', 'ativo')
    list_filter = ('especialidade', 'ativo')
    search_fields = ('nome', 'email', 'telefone')
