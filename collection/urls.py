from django.urls import path
from .views import create_or_update_collection

urlpatterns = [
    path('collections/new/', create_or_update_collection, name='create_collection'),
    path('collections/<int:collection_id>/edit/', create_or_update_collection, name='update_collection'),
]
