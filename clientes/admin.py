from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'data_nascimento', 'data_cadastro')
    search_fields = ('nome', 'telefone', 'email', 'cpf')
    list_filter = ('data_cadastro',)
