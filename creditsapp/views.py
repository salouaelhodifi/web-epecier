from django.shortcuts import render
from .models import Credit, Paiement

def credit_list(request):
    credits = Credit.objects.all()
    context = {'credits': credits}
    return render(request, 'credit_list.html', context)

def paiement_list(request):
    paiements = Paiement.objects.all()
    context = {'paiements': paiements}
    return render(request, 'paiement_list.html', context)
