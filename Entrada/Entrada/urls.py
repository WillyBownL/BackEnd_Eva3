"""Entrada URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from appEntrada import views as Entrada
from appCliente import views as Cliente
from appConcierto import views as Concierto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Entrada.index),

    # App Cliente

    path('Cliente/' , Cliente.index),
    path('Cliente/lista/', Cliente.lista, name='lista'),
    path('Cliente/agregar/', Cliente.agregar, name='agregar'),
    path('Cliente/editar/<int:id>/', Cliente.editar, name='editar'),
    path('Cliente/eliminar/<int:id>/', Cliente.eliminar, name='eliminar'),

    # App Concierto

    path('Concierto/', Concierto.index),
    path('Concierto/conciertos/', Concierto.listadoConcierto, name='listadoConcierto'),
    path('Concierto/agregarConcierto/', Concierto.agregarConcierto),
    path('Concierto/actualizarConcierto/<int:id>', Concierto.actualizarConcierto),
    path('Concierto/eliminarConcierto/<int:id>', Concierto.eliminarConcierto),

    # App Entrada
    path('Entrada/lista/', Entrada.lista_entradas, name='listaEntrada'),
    path('Entrada/agregar/', Entrada.agregar_entrada),
    path('Entrada/editar/<int:id>', Entrada.editarEntrada),
    path('Entrada/eliminar/<int:id>', Entrada.eliminarEntrada),


]
