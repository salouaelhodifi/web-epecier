from django import forms
from fournisseurApp.models import Fournisseur

class FornisseurForm(forms.ModelForm):
    class Meta:
        model= Fournisseur
        fields="__all__"