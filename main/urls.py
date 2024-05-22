from django.urls import path
from .views import create_recipe, home, recipe_list, delete_recipe

urlpatterns = [
    path('', home, name='home'),
    path('recipe-list', recipe_list, name='recipe_list'),
    path('create-recipe', create_recipe, name='create_recipe'), 
    path('delete/<int:id>', delete_recipe, name='delete_recipe'),
]