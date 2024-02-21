from django import forms
from .models import Ativo


class AtivoForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = ['name', 'tipo', 'quantity', 'preco_unitario']
