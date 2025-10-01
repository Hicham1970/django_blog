from django.urls import path
from .views import home

urlpatterns = [
    path('', home),  # URL racine de l'app
   
]