from django.shortcuts import render
from main.models import Recipe
from .models import ReviewItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/auth/login')
def recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    review_list = ReviewItem.objects.filter(recipe=recipe)
    context = {
        'recipe':recipe,
        'reviews':review_list,
        'recipe_id': recipe_id
    }

    return render(request, "review.html", context)

@csrf_exempt
def review(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            recipe_id = request.POST['reviewForm']
            recipe = Recipe.objects.filter(pk=recipe_id)
            ReviewItem.objects.get_or_create(user=request.user, recipe=recipe[0], review=request.POST['review'])
    return HttpResponseRedirect(reverse('recipe_view', kwargs={'recipe_id': recipe_id})+"#reviewElement")
