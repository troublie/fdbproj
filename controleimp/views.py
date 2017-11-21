from django.shortcuts import render, get_object_or_404, redirect
from .models import Moeda, TermoPagto, Cliente, Pedido
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

def pedidos_list(request):
    pedido = Pedido.objects.all().order_by("data")
    return render(request, "controleimp/pedidos_list.html", {"pedidos": pedido})


def termo_detail(request, pk):
    termo = get_object_or_404(TermoPagto, pk=pk)
    return render(request, 'controleimp/termo_detail.html', {'termo': termo})


def termo_new(request):
    form = TermoPagtoForm()
    if request.method == "POST":
        form = TermoPagtoForm(request.POST)
    if form.is_valid():
        termo = form.save(commit=False)
        termo.save()
        return redirect("termo_detail", pk=termo.pk)
    else:
        form = TermoPagtoForm()
    return render(request, 'controleimp/termo_new.html', {'form': form})


def termo_edit(request, pk):
    termo = get_object_or_404(TermoPagto, pk=pk)
    form = TermoPagtoForm()
    if request.method == "POST":
        form = TermoPagtoForm(request.POST, instance=termo)
    if form.is_valid():
        termo = form.save(commit=False)
        termo.save()
        return redirect('termo_detail', pk=termo.pk)
    else:
        form = TermoPagtoForm(instance=termo)
    return render(request, 'controleimp/termo_edit.html', {'form': form})


def termo_remove(request, pk):
    termo = get_object_or_404(TermoPagto, pk=pk)
    termo.delete()
    return redirect('termo_list')
