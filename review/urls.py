from django.urls import path
from . import views

urlpatterns = [
    path('<int:recipe_id>', views.recipe, name="recipe_view"),
    path('review', views.review, name="recipe_review")
]