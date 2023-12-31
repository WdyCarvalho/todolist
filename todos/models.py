from django.db import models
from datetime import date

# Create your models here.

"""
Aqui, em models, a classe representa uma tabela. As colunas da tabela são os atributos da classe.
Observe abaixo:
"""

class Todo(models.Model): # models.Model indica de onde essa classe herdou suas características
    #As variáveis(atributos) são as colunas da tabela:
    titulo = models.CharField(max_length = 100, null = False, blank = False )
    data_criacao_tarefa = models.DateField(auto_now = True, null = False, blank = False)
    data_entrega_tarefa = models.DateField(null = False, blank = False)
    data_finalizacao_tarefa = models.DateField(null = True)

    #coloca as tarefas em ordem de acordo com a data de entrega
    class Meta:
        ordering = ["data_entrega_tarefa"]

    def marcar_como_completo(self):
        if not self.data_finalizacao_tarefa:
            self.data_finalizacao_tarefa = date.today()
            self.save()