from django.urls import path
from . import views
urlpatterns = [
    path('<int:recipe_id>', views.recipe, name="recipe_view"),
    # path('review', views.review, name="recipe_review"),
    path('submit', views.review, name="recipe_review"),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('recipe/<int:recipe_id>/', views.recipe, name='recipe_view'),
    path('select-collection/<int:recipe_id>/', views.select_collection, name='select_collection'),

]