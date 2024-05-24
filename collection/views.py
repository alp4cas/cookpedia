from django.shortcuts import render, redirect
from .forms import CollectionForm
from .models import Collection
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from main.models import Recipe
from django.core.exceptions import PermissionDenied

@login_required(login_url="user_auth:login")
def remove_recipe(request, collection_id, recipe_id):
    collection = get_object_or_404(Collection, id=collection_id, user=request.user)
    recipe = get_object_or_404(Recipe, id=recipe_id)
    collection.recipes.remove(recipe)
    return redirect('collection:collection_detail', collection_id=collection_id)

@login_required(login_url="user_auth:login")
def user_collections(request):
    collections = Collection.objects.filter(user=request.user) 
    recipes = Recipe.objects.all()
    return render(request, 'user_collections.html', {'collections': collections, 'recipes': recipes})

@login_required(login_url="user_auth:login")
def create_or_update_collection(request, collection_id=None):
    if collection_id:
        collection = get_object_or_404(Collection, id=collection_id)
        if request.user != collection.user:
            raise PermissionDenied 
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

    recipes = Recipe.objects.all()
    collection_recipes = collection.recipes.all() if collection else []

    return render(request, 'create_or_update_collection.html', {
        'form': form,
        'collection': collection,
        'recipes': recipes,
        'collection_recipes': collection_recipes
    })



@login_required(login_url="user_auth:login")
def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    if request.user != collection.user:
        raise PermissionDenied 
    return render(request, 'collection_detail.html', {'collection': collection})

@login_required(login_url="user_auth:login")
@require_POST
def delete_collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)

    if request.user != collection.user:
        raise PermissionDenied 

    collection.delete()
    return redirect('collection:user_collections')

def get_collection_json(request):
    collection_item = Collection.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', collection_item))

def get_recipes_json(request):
    recipe_item = Recipe.objects.all()
    return HttpResponse(serializers.serialize('json', recipe_item))

@csrf_exempt
def add_collection_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        recipes = request.POST.getlist("recipes[]") 
        user = request.user
        new_collection = Collection.objects.create(name=name, description=description, user=user)
        new_collection.recipes.set(recipes) 
        new_collection.save()
        return JsonResponse({'status': 'created'}, status=201)

    return HttpResponseNotFound()