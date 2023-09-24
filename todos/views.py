from django.views.generic import ListView, CreateView, UpdateView #Essas importações permitem listar, criar(cadastrar) e alterar tarefas
from django.urls import reverse_lazy #recebe os nomes das rotas

from .models import Todo

class TodoListView(ListView): #a classe TodoListView utiliza como argumento a importação ListView
    model = Todo #Todo é o nome do banco de dados

class TodoCreateView(CreateView):
    model = Todo
    fields = ["titulo", "data_entrega_tarefa"] #a variável field é padrão do python. Ela gera formulários automaticamente
    success_url = reverse_lazy("todo_list") #Depois de cadastrar, redireciona para a rota com nome todo_list

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["titulo", "data_entrega_tarefa"]
    success_url = reverse_lazy("todo_list")