from django.core.management.base import BaseCommand
from clientes.aniversarios import aniversariantes_hoje
import pywhatkit
import time

class Command(BaseCommand):
    help = 'Envia mensagem de aniversário via WhatsApp para clientes aniversariantes do dia.'

    def handle(self, *args, **options):
        mensagem_padrao = (
            "Olá, {nome}! 🎉 A equipe da Clínica Silvia Vaz Estética Avançada deseja um FELIZ ANIVERSÁRIO! "
            "Que o seu dia seja incrível! Temos uma surpresa especial para você, venha conferir! 🎁"
        )

        aniversariantes = aniversariantes_hoje()
        total = aniversariantes.count()
        self.stdout.write(self.style.SUCCESS(f"Encontrados {total} aniversariantes no dia de hoje."))

        for cliente in aniversariantes:
            numero = cliente.telefone
            if not numero.startswith('+'):
                numero = '+55' + numero  # Ajuste conforme o seu padrão de banco
            mensagem = mensagem_padrao.format(nome=cliente.nome.split()[0])
            try:
                pywhatkit.sendwhatmsg_instantly(
                    numero,
                    mensagem,
                    wait_time=15,
                    tab_close=True,
                    close_time=30
                )
                self.stdout.write(self.style.SUCCESS(f"Mensagem enviada para {cliente.nome} ({numero})"))
                time.sleep(25)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erro ao enviar para {cliente.nome} ({numero}): {e}"))
