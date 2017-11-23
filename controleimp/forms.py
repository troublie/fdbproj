from django import forms

from .models import TermoPagto, Pedido

class TermoPagtoForm(forms.ModelForm):

    class Meta:
        model = TermoPagto
        fields = 'termo',

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = "cliente", "numero", "moeda", "valor", "termo",