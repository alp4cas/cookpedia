from django.urls import path, include
from .views import *

app_name = 'main'
urlpatterns = [
    path('', home, name='home'),
    path('manage-recipe', manage_recipe, name='manage_recipe'),
    path('recipe-list', recipe_list, name='recipe_list'),
    path('create-recipe', create_recipe, name='create_recipe'), 
    path('delete/<int:id>', delete_recipe, name='delete_recipe'),
    path('auth/', include('user_auth.urls', namespace='user_auth')),
    path('favorite/', include('favorite.urls', namespace='favorite')), 
    path('approve-recipe/<int:recipe_id>/', approve_recipe, name='approve_recipe'),
    path('reject-recipe/<int:recipe_id>/', reject_recipe, name='reject_recipe'),
    path('recipes/<str:param>', get_recipe, name='get_recipe'),
]
