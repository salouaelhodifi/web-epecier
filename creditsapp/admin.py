from django.contrib import admin
from .models import Credit, Paiement

@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['id_client', 'credit', 'date_credit', 'solde']

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ['credit', 'montant', 'date_paiement']
