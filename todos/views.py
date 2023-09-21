from django.shortcuts import render
from django.http import HttpResponse #HttpResponse  é o recurso do django que servidor a resposnder ao request.

# Create your views here.

def home(request): #request é 'Solicitação'. pergunta algo ao servidor
    #return HttpResponse ("Teste com HttpResponse") #Poderia ser assim
    return render(request, "todos/home.html") #Mas assim, renderiza páginas web
  
    """
    a pasta templates não aparece no endereço acima
    porque o django já procura pela página html em uma pasta chamada templates

    'return render' renderiza a página htlm em: templates/todos/home.html
    """
     