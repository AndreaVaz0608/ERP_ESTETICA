# campanhas/management/commands/send_scheduled_messages.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from campanhas.models import MensagemAgendada

class Command(BaseCommand):
    help = 'Envia as mensagens agendadas para os destinatários.'

    def handle(self, *args, **options):
        now = timezone.now()
        mensagens = MensagemAgendada.objects.filter(
            ativo=True,
            data_disparo__lte=now
        )

        for mensagem in mensagens:
            self.stdout.write(self.style.SUCCESS(f'Enviando: {mensagem.titulo} ({mensagem.get_tipo_display()})'))
            for destinatario in mensagem.destinatarios.all():
                # Aqui você coloca a integração de envio: WhatsApp, e-mail, SMS...
                self.stdout.write(f"Mensagem para: {destinatario}")
                # Exemplo fictício:
                # send_whatsapp(destinatario.telefone, mensagem.mensagem)

            mensagem.ativo = False  # Marcar como enviado (opcional)
            mensagem.save()
