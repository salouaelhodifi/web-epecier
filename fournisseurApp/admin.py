from django.contrib import admin
from .models import Fournisseur,Chiffre_Affaire

@admin.register(Fournisseur)
class Request_Fournisseur(admin.ModelAdmin):
    list_display = ['nom_fournisseur', 'date_emprunt', 'Valeur_Dette', 'date_De_remboursement' ]
@admin.register(Chiffre_Affaire)
class Request_Chiffre_Affaire(admin.ModelAdmin):
    list_display = ['ca', 'periode' ]