from django.db import models

 
class Fournisseur(models.Model):
    
    nom_fournisseur= models.CharField(max_length=50)
    date_emprunt=models.DateField()
    Valeur_Dette = models.DecimalField(max_digits=8, decimal_places=2)
    date_De_remboursement = models.DateField()

    def __str__(self):
        return self.nom_fournisseur +" "+"dont le montant  est "+ str(self.Valeur_Dette)

class Chiffre_Affaire(models.Model):
    ca=models.DecimalField(max_digits=12, decimal_places=3)
    periode=models.DateField()

    def __str__(self):
        return  "le chiffre d'affaire réalisé  est "+ str(self.ca)
    











 

