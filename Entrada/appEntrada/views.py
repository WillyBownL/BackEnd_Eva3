from django.shortcuts import render

# Create your views here.


def MenuPrincipal(request):
    return render(request, 'appEntrada/index.html')