from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', status=201, context={'name': 'Gabriel Teodoro'})

def sobre(request):
    return HttpResponse('SOBRE!!!')

def contato(request):
    return render(request, 'recipes/contato.html')