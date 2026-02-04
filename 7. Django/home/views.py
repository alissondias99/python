from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print('home')
    return render(
        request, 
        'home/home.html' # template name requerido pelo request
    )