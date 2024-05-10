from django.urls import path, include
from .views import create_recipe, home, recipe_list, delete_recipe

app_name = 'main'
urlpatterns = [
    path('', home, name='home'),
    path('approve-recipe/<int:recipe_id>/', approve_recipe, name='approve_recipe'),
    path('reject-recipe/<int:recipe_id>/', reject_recipe, name='reject_recipe'),
    path('recipe-list', recipe_list, name='recipe_list'),
    path('create-recipe', create_recipe, name='create_recipe'), 
    path('delete/<int:id>', delete_recipe, name='delete_recipe'),
    path('auth/', include('user_auth.urls', namespace='user_auth')),
    path('favorite/', include('favorite.urls', namespace='favorite')), 
]