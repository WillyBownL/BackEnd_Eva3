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

# Vista para editar una entrada
def editarEntrada(request, id):
    icliente = Entrada.objects.get(id = id)
    form = FormEntrada (instance=Entrada)
    if request.method == 'POST':
        form = FormEntrada(request.POST, instance=Entrada)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form= FormEntrada(instance=Entrada)
    data = {'form':form}
    return render(request, 'appCliente/agregar.html', data)

# Vista para eliminar una entrada
def eliminarEntrada(request, id):
    ientrada = Entrada.objects.get(id=id)
    ientrada.delete()
    return redirect('lista')
