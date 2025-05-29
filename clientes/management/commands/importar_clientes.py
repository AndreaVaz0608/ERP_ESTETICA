import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from clientes.models import Cliente

class Command(BaseCommand):
    help = 'Importa clientes de um arquivo CSV, exigindo apenas o nome'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        count = 0
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get('nome'):
                    self.stdout.write(self.style.WARNING("Cliente sem nome ignorado"))
                    continue

                data_nascimento = None
                if row.get('data_nascimento'):
                    try:
                        data_nascimento = datetime.strptime(row['data_nascimento'], '%Y-%m-%d').date()
                    except ValueError:
                        self.stdout.write(self.style.WARNING(f"Data inválida para {row['nome']}: {row['data_nascimento']}"))

                cliente, created = Cliente.objects.get_or_create(
                    telefone=row.get('telefone') or '',
                    defaults={
                        'nome': row['nome'],
                        'email': row.get('email') or '',
                        'data_nascimento': data_nascimento,
                        'endereco': row.get('endereco') or '',
                        'cpf': row.get('cpf') or '',
                        'categoria': row.get('categoria') or '',
                    }
                )
                if created:
                    count += 1
        self.stdout.write(self.style.SUCCESS(f'{count} clientes importados com sucesso (exigindo apenas nome)!'))
