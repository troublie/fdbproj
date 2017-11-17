from django.shortcuts import render


def index(request):
    return render(request, "controleimp/index.html")


def cadastros(request):
    return render(request, "controleimp/cadastros.html")


def pedidos(request):
    return render(request, "controleimp/pedidos.html")
