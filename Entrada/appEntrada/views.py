from django.shortcuts import render,render
from appCliente.models import Cliente
from appConcierto.models import Concierto
from appEntrada.models import Entrada

# Create your views here.


def MenuPrincipal(request):
    return render(request, 'appEntrada/index.html')

def listadoEntrada(request):
    entradas = Entrada.objects.all()
    data = {'entradas': entradas}
    return render(request, 'appEntrada/listadoEntrada.html')

def detalleEntrada(request, id):
    return render(request, 'appEntrada/detalleEntrada.html', {'id': id})