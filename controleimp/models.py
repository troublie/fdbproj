from django.db import models
from django.utils import timezone


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
    moeda = models.CharField(max_length=3)
    valor = models.DecimalField
    termo = models.CharField(max_length=3)

    def save(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.title
