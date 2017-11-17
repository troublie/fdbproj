from django.shortcuts import render
from django.utils import timezone
from .models import Moeda


def index(request):
    return render(request, "controleimp/index.html")


def cadastros(request):
    return render(request, "controleimp/cadastros.html")


def pedidos(request):
    return render(request, "controleimp/pedidos.html")


def moeda_list(request):
    moedas = Moeda.objects.filter().order_by("codigo")
    return render(request, "controleimp/moeda_list.html", {"moedas": moedas})
