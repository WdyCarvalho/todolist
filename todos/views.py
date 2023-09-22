from django.shortcuts import render

from .models import Todo

def todo_list(request):
    #todos, abaixo, são as tarefas
    todos = Todo.objects.all() #objects é o método que busca dados no banco de dados   
    return render(request, "todos/todo_list.html", {"todos": todos})#todos entre aspas sou eu que dou o nome. poderia ser tarefas