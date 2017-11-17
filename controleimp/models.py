from django.db import models
from django.utils import timezone
from decimal import Decimal

class TermoPagto(models.Model):
    termo = models.IntegerField

class Moeda(models.Model):
    codigo = models.CharField(max_length=3)
    descricao = models.CharField(max_length=30)


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)

    def save(self):
        self.save()

    def __str__(self):
        return self.title


class Pedido(models.Model):
    author = models.ForeignKey('auth.User')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    data = models.DateTimeField
    moeda = models.ForeignKey(Moeda, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2,
               default=Decimal(0.00))
    termo = models.ForeignKey(TermoPagto, on_delete=models.CASCADE)

    def save(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.title
