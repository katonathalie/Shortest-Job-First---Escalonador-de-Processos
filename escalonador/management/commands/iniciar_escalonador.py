from django.core.management.base import BaseCommand, CommandError
from escalonador.models import Processo
from datetime import datetime
import time

class Command(BaseCommand):
    help = 'Inicia o escalonador'

    def handle(self, *args, **options):
        contador_processos = 0
        somador_tempo_espera = 0

        while True:
            try:
                processos = Processo.objects.all()
                for p in processos:
                    p = self.seleciona_processo()
                    escala_execucao = p.tamanho + 10
                    contador_processos += 1
                    tempo_espera = datetime.today() - p.chegada
                    somador_tempo_espera += tempo_espera.seconds
                    media = somador_tempo_espera/contador_processos

                    print('Processo selecionado: ' + p.nome)
                    print('Tempo de execução: %d segundos.' % escala_execucao)
                    print('Hora de Chegada na Lista de Pronto ------> ' + p.chegada.strftime('%Y-%m-%d %H:%M:%S'))
                    print('Hora que o processo foi escolhido -------> ' + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
                    print('\nTempo de espera: %d min e %d segundos aprox.' % ((tempo_espera.seconds/60), (tempo_espera.seconds%60)))
                    print('\n\tTempo médio de espera -> %.2f segundos.\n\n' % media)

                    p.delete()

                    time.sleep(escala_execucao)

            except CommandError:
                print('\nEscalonador interrompido.')
                break


    def seleciona_processo(self):
        try:
            processo = Processo.objects.earliest('tamanho', 'chegada')

        except CommandError:
            raise CommandError('Comando nao executado')
        return processo


