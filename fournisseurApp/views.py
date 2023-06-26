from django.shortcuts import render,redirect
from .models import Fournisseur,Chiffre_Affaire
from .forms import FornisseurForm

def fournisseurs(request):
    if request.method=="POST":
        form= FornisseurForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/fournisseur_show")
            except:
                pass
    else:
            form=FornisseurForm()
    return render(request,'fournisseur_form.html',{'form': form}) 

def show(request):
    fournisseurs = Fournisseur.objects.all()
    context = {'fournisseurs': fournisseurs}
    return render(request, 'fournisseur_show.html', context)


def Chiffre_Affaire_list(request):
    Chiffres_Affaire = Chiffre_Affaire.objects.all()
    context = {'Chiffres_Affaire': Chiffres_Affaire}
    return render(request, 'ca.html', context)  


