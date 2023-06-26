from django import forms
from produitsApp.models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model= Produit
        fields="__all__"