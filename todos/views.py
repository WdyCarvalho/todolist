from datetime import date

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View #Essas importações permitem listar, criar(cadastrar), alterar e excluir tarefas
from django.urls import reverse_lazy #recebe os nomes das rotas
from django.shortcuts import get_object_or_404, redirect

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

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.data_finalizacao_tarefa = date.today()
        todo.save()
        return redirect("todo_list")
    