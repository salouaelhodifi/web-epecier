from django.db import models
from django.contrib import admin

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    quantite = models.PositiveIntegerField()
    libelle = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle +" "+"dont le prix est "+ str(self.prix)+" DH"
    
    class Meta:
        db_table="Produits"

class ProduitAdmin(admin.ModelAdmin):
    list_display=('prix','quantite','libelle','categorie')
    list_filter=('libelle','prix',)
    search_fields=['libelle']



