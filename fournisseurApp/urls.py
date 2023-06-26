from django.urls import path
from fournisseurApp import views

urlpatterns = [
    path('fournisseurs',views.fournisseurs,),
    path('fournisseur_show',views.show, name='fournisseurs'),
    path('Chiffres_Affaire/', views.Chiffre_Affaire_list, name='ca'),
]
