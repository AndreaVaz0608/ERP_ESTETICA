from django.contrib import admin
from .models import Agendamento

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'data_hora', 'listar_servicos', 'profissional', 'confirmado', 'criado_em')
    search_fields = ('cliente__nome', 'profissional')
    list_filter = ('confirmado', 'data_hora', 'profissional')

    def listar_servicos(self, obj):
        return ", ".join(s.nome for s in obj.servicos.all())
    listar_servicos.short_description = 'Serviços'
