from django.db import models
from django.utils import timezone
from decimal import Decimal
from datetime import datetime
from django.utils.formats import date_format


class TermoPagto(models.Model):
    termo = models.IntegerField(blank=False)

    def salvar(self):
        self.salvar()

    def __str__(self):
        return str(self.termo)


class Moeda(models.Model):
    codigo = models.CharField(max_length=3)
    descricao = models.CharField(max_length=30)

    def salvar(self):
        self.salvar()

    def __str__(self):
        return self.codigo


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.EmailField(default="example@example.com")

    def salvar(self):
        self.salvar()

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    author = models.ForeignKey('auth.User')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    data = models.DateTimeField(blank=True, null=True, default=timezone.now, editable=False)
    moeda = models.ForeignKey(Moeda, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2,
                                default=Decimal(0.00))
    termo = models.ForeignKey(TermoPagto, on_delete=models.CASCADE)

    def salvar(self):
        self.data = timezone.now()
        self.salvar()

    def __str__(self):
        return self.numero
