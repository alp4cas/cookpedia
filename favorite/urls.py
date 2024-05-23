from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.favorite_view, name='favorite_view'),
    path('add_to_favorite/<int:recipe_id>/', views.add_to_favorite, name='add_to_favorite'),
    path('remove/<int:recipe_id>/', views.remove_from_favorite, name='remove_from_favorite')
]
