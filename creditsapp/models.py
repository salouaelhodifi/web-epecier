from django.db import models

class Credit(models.Model):
    id_client = models.CharField(max_length=10, primary_key=True)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    date_credit = models.DateTimeField(auto_now_add=True)
    date_echeance=models.DateField()
   
    def __str__(self):
        return f"{self.id_client} - {self.credit}DH"

    def solde(self):
        paiements = self.paiements.all()
        total_paiements = sum(p.montant for p in paiements)
        solde = self.credit - total_paiements
        return solde
        
class Paiement(models.Model):
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE, related_name='paiements')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.credit} - {self.montant}DH"