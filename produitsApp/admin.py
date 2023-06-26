from django.contrib import admin
from .models import Produit,ProduitAdmin
admin.site.register(Produit,ProduitAdmin)
from.models import Categorie
admin.site.register(Categorie)

