from django.db import models
from django.contrib import admin
# Create your models here.
class Client(models.Model):
    cid=models.CharField(max_length=50)
    nom=models.CharField(max_length=25)
    prenom=models.CharField(max_length=25)
    telephone=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    def __str__(self):
        return "%s" %(self.nom)    
    class Meta:
        db_table="clients"
    
class ClientAdmin(admin.ModelAdmin):
    list_display=('cid','nom','prenom', 'telephone','email')
    list_filter=('nom',)
    search_fields=['cid','nom','telephone']
