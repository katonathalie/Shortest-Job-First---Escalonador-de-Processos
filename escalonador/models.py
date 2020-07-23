from django.db import models

class ProcessoManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(tamanho__icontains=query) |
            models.Q(chegada__icontains=query)
        )

class Processo(models.Model):

    nome = models.CharField(max_length=20, unique=True)
    chegada = models.DateTimeField(auto_now_add=True)
    tamanho = models.IntegerField(null=False, blank=False)

    objects = ProcessoManager()

    class Meta:
        db_table = 'Lista de Pronto'
        ordering = ['tamanho', 'chegada']
