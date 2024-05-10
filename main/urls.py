from django.urls import path
from .views import create_recipe, home, main

urlpatterns = [
    path('', home, name='home'),
    path('main', main, name='main'),
    path('create-recipe', create_recipe, name='create_recipe'), 
]
