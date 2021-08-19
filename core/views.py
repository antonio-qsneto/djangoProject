from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotativo
from django.http import HttpResponse
from .form import PessoaForm, VeiculoForm, MovRotativoForm



def home(request):
    return HttpResponse('ola mundo')


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas, 'form': form})


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect("core_lista_pessoas")


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect("core_lista_veiculos")


def listaMovRot(request):
    movrot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'movrot': movrot, 'form': form}
    return render(request, 'core/lista_movRotativo.html', data)

def movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect("core_lista_movrot")
