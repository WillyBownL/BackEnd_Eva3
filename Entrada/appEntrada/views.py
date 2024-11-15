from django.shortcuts import render, redirect
from appEntrada.models import Entrada
from appEntrada.forms import FormEntrada


def index(request):
    return render(request, 'appEntrada/index.html')

# Vista para listar las entradas
def lista_entradas(request):
    entradas = Entrada.objects.all()
    data = {'entradas': entradas}
    return render(request, 'appEntrada/listadoEntrada.html', data)

# Vista para agregar una nueva entrada
def agregar_entrada(request):
    if request.method == 'POST':
        form = FormEntrada(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaEntrada')
    else:
        form = FormEntrada()
    
    data = {'form': form}
    return render(request, 'appEntrada/agregarEntrada.html', data)
