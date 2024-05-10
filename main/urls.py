from django.urls import path
from .views import create_recipe, home, main, delete_recipe

urlpatterns = [
    path('', home, name='home'),
]