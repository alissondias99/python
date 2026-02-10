from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(
        request, 
        'home/index.html', # template name requerido pelo request, vai recuperar os dados de base->global->base.html
        {
            'text': 'Estamos na home' # ← context, define comportamentos da página
        }
    )