from django.shortcuts import render, get_object_or_404, redirect
from main.models import Recipe
from .models import ReviewItem
from collection.models import Collection
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/auth/login')
def recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    review_list = ReviewItem.objects.filter(recipe=recipe)
    collections = Collection.objects.filter(user=request.user)
    context = {
        'recipe': recipe,
        'reviews': review_list,
        'recipe_id': recipe_id,
        'collections': collections
    }
    return render(request, "review.html", context)

@login_required(login_url='/auth/login')
def select_collection(request, recipe_id):
    collections = Collection.objects.filter(user=request.user)
    recipe = Recipe.objects.get(pk=recipe_id)
    if request.method == 'POST':
        selected_collections = request.POST.getlist('collections')
        for collection_id in selected_collections:
            collection = Collection.objects.get(id=collection_id)
            collection.recipes.add(recipe)
        return redirect('recipe_view', recipe_id=recipe_id)
    return render(request, 'select_collection.html', {'collections': collections, 'recipe': recipe})

@csrf_exempt
def review(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            recipe_id = request.POST['reviewForm']
            recipe = Recipe.objects.filter(pk=recipe_id)
            ReviewItem.objects.get_or_create(user=request.user, recipe=recipe[0], review=request.POST['review'])
    return HttpResponseRedirect(reverse('recipe_view', kwargs={'recipe_id': recipe_id})+"#reviewElement")

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(ReviewItem, id=review_id, user=request.user)
    recipe_id = review.recipe.id
    review.delete()
    return HttpResponseRedirect(reverse('recipe_view', kwargs={'recipe_id': recipe_id})+"#reviewElement")
