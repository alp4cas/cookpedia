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
    path('set-recipe-status/<int:recipe_id>/<str:status>/', set_recipe_status, name='set_recipe_status'),
    path('recipes/<str:param>', get_recipe, name='get_recipe'),
    path('verify-user/<int:user_id>/', verify_user, name='verify_user'),
]
