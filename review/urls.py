from django.urls import path
from . import views
urlpatterns = [
    path('<int:recipe_id>', views.recipe, name="recipe_view"),
    # path('review', views.review, name="recipe_review"),
    path('submit', views.review, name="recipe_review"),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('add_to_collection/', views.add_to_collection, name='add_to_collection'),

]