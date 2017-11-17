from django.contrib import admin
from .models import Cliente, Pedido, Moeda, TermoPagto

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Moeda)
admin.site.register(TermoPagto)