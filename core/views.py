from django.shortcuts import render
from .models import Pessoa, Veiculo, movRotativo
from django.http import HttpResponse


def home(request):
    return HttpResponse('ola mundo')


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def listaMovRot(request):
    movrot = movRotativo.objects.all()
    return render(request, 'core/lista_movRotativo.html', {'movrot': movrot})