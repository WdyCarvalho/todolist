from django.views.generic import ListView

from .models import Todo

class TodoListView(ListView): #a classe TodoListView utiliza como argumento a importação ListView
    model = Todo #Todo é o nome do banco de dados