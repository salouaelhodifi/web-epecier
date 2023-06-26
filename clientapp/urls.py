from django.urls import path
from clientapp import views

urlpatterns = [
    path('clients',views.clients, name='add'),
    path('show',views.show, name='clients'),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy),
]