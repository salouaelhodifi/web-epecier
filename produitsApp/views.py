from django.shortcuts import render,redirect
from produitsApp.formulaire import ProduitForm
from .models import Produit
def produits(request):
    if request.method=="POST":
        form= ProduitForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/product")
            except:
                pass
    else:
            form=ProduitForm()
    return render(request,'indice.html',{'form': form})
def show(request):
    produits= Produit.objects.all()
    return render(request,'product.html',{'produits': produits })
