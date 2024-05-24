from django.shortcuts import render
from .models import FavoriteItem
from main.models import Recipe
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url='/auth/login')
def favorite_view(request):
    if request.user.is_authenticated:
        user = request.user
        favorite_items = FavoriteItem.objects.filter(user=user)
        favorite_recipes = [item.recipe for item in favorite_items]
    else:
        favorite_recipes = []

    context = {
        'favorite_recipes': favorite_recipes
    }
    return render(request, 'favorite.html', context)

@login_required
def add_to_favorite(request, recipe_id):
    if request.user.is_authenticated:
        recipe = Recipe.objects.get(id=recipe_id)
        FavoriteItem.objects.get_or_create(user=request.user, recipe=recipe)
        return JsonResponse({'message': 'Recipe added to favorites'})
    else:
        return JsonResponse({'message': 'Authentication required to add to favorites'}, status=401)


def remove_from_favorite(request, recipe_id):
    if request.user.is_authenticated:
        recipe = Recipe.objects.get(id=recipe_id)
        FavoriteItem.objects.filter(user=request.user, recipe=recipe).delete()
    return JsonResponse({'message': 'Recipe removed from wishlist'})



