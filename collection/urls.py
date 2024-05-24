from django.urls import path
from .views import create_or_update_collection,collection_detail,user_collections,delete_collection

app_name = 'collection'
urlpatterns = [
    path('collections/', user_collections, name='user_collections'),
    path('new/', create_or_update_collection, name='create_collection'),
    path('<int:collection_id>/edit/', create_or_update_collection, name='update_collection'),
    path('collection/<int:collection_id>/', collection_detail, name='collection_detail'),
    path('collection/<int:collection_id>/delete/', delete_collection, name='delete_collection'),
]
