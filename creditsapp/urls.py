from django.urls import path
from creditsapp import views

urlpatterns = [
    path('credits/', views.credit_list, name='credit_list'),
    path('paiements/', views.paiement_list, name='paiement_list'),
]