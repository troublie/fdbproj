from django.shortcuts import render
from django.utils import timezone
from .models import Moeda, TermoPagto, Cliente
from .forms import TermoPagtoForm


def index(request):
    return render(request, "controleimp/index.html")


def cadastros(request):
    return render(request, "controleimp/cadastros.html")


def pedidos(request):
    return render(request, "controleimp/pedidos.html")


def moeda_list(request):
    moedas = Moeda.objects.all().order_by("codigo")
    return render(request, "controleimp/moeda_list.html", {"moedas": moedas})


def termo_list(request):
    termos = TermoPagto.objects.all().order_by("termo")
    return render(request, "controleimp/termo_list.html", {"termos": termos})


def cliente_list(request):
    clientes = Cliente.objects.all().order_by("nome")
    return render(request, "controleimp/cliente_list.html", {"clientes": clientes})


def termo_new(request):
    if request.method == "POST":
        form = TermoPagtoForm(request.POST)
    if form.is_valid():
        termo = form.save(commit=False)
        termo.save()
        return redirect('termo_list')
    else:
        form = TermoPagtoForm()
    return render(request, 'controleimp/termo_edit.html', {'form': form})
