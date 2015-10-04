from django import forms
from cadastro.models import ItemCardapio


class ItemCardapioForm(forms.ModelForm):

    class Meta:
        model = ItemCardapio
        exclude=[]
        fields=[]
