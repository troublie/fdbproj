from django import forms

from .models import TermoPagto

class TermoPagtoForm(forms.ModelForm):

    class Meta:
        model = TermoPagto
        fields = 'termo',