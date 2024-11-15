from django.shortcuts import render, redirect
from appEntrada.models import Entrada
from appEntrada.forms import FormEntrada  

# Vista para listar las entradas
def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'appEntrada/lista.html', {'entradas': entradas})

# Vista para agregar una nueva entrada
def agregar_entrada(request):
    if request.method == 'POST':
        form = FormEntrada(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_entradas')
    else:
        form = FormEntrada()
    return render(request, 'appEntrada/agregar.html', {'form': form})
