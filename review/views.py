from django.shortcuts import render
from main.models import Recipe
from .models import ReviewItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import get_object_or_404
from collection.models import Collection

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

@csrf_exempt
@login_required
def add_to_collection(request):
    if request.method == "POST":
        recipe_id = request.POST.get('recipe_id')
        collections = request.POST.getlist('collections')

        print(f"Received recipe_id: {recipe_id}")
        print(f"Received collections: {collections}")

        recipe = get_object_or_404(Recipe, id=recipe_id)
        
        for collection_id in collections:
            collection = get_object_or_404(Collection, id=collection_id, user=request.user)
            collection.recipes.add(recipe)
            collection.save()
            print(f"Added recipe {recipe_id} to collection {collection_id}")

        return JsonResponse({'message': 'Recipe added to collections successfully!'})
    
    return JsonResponse({'message': 'Invalid request'}, status=400)

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
