from django.shortcuts import render, redirect
from .forms import CollectionForm
from .models import Collection
from django.shortcuts import get_object_or_404

def create_or_update_collection(request, collection_id=None):
    if collection_id:
        collection = get_object_or_404(Collection, id=collection_id, user=request.user)
        if request.user != collection.user:
            return redirect('collections')  
    else:
        collection = None

    if request.method == 'POST':
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid():
            new_collection = form.save(commit=False)
            new_collection.user = request.user
            new_collection.save()
            form.save_m2m()  
            return redirect('collection_detail', collection_id=new_collection.id)
    else:
        form = CollectionForm(instance=collection)

    return render(request, 'create_or_update_collection.html', {'form': form, 'collection': collection})
