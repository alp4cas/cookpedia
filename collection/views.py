from django.shortcuts import render, redirect
from .forms import CollectionForm
from .models import Collection
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST

@login_required(login_url="user_auth:login")
def user_collections(request):
    collections = Collection.objects.filter(user=request.user)  # Retrieve collections for the logged-in user
    return render(request, 'user_collections.html', {'collections': collections})

@login_required(login_url="user_auth:login")
def create_or_update_collection(request, collection_id=None):
    if collection_id:
        collection = get_object_or_404(Collection, id=collection_id)
        if request.user != collection.user:
            raise PermissionDenied  # Prevent editing someone else's collection
    else:
        collection = None

    if request.method == 'POST':
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid():
            new_collection = form.save(commit=False)
            new_collection.user = request.user
            new_collection.save()
            form.save_m2m()
            return redirect('collection:collection_detail', collection_id=new_collection.id)
    else:
        form = CollectionForm(instance=collection)

    return render(request, 'create_or_update_collection.html', {'form': form, 'collection': collection})

@login_required(login_url="user_auth:login")
def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    if request.user != collection.user:
        raise PermissionDenied  # Ensures only the owner can view the collection details

    return render(request, 'collection_detail.html', {'collection': collection})

@login_required(login_url="user_auth:login")
@require_POST
def delete_collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)

    if request.user != collection.user:
        raise PermissionDenied 

    collection.delete()
    return redirect('collection:user_collections')
