from django import forms
from .models import Processo

class CadastrarProcessoForm(forms.ModelForm):

    class Meta:
        model = Processo
        fields = ['nome', 'tamanho']