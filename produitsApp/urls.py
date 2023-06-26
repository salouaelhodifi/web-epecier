from django.urls import path
from produitsApp import views

urlpatterns = [
        path('produits',views.produits,name='product'),
        path('products',views.show, name ='products' ),
]