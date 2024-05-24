from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .models import Recipe

from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from main.forms import RecipeForm
from .models import Recipe

from django.contrib.auth.decorators import login_required


@login_required(login_url='auth/login')
def home(request):
    return render(request, 'homepage.html')

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def show_recipe(request):
    data = Recipe.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_recipe(request):  
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))  
    else:
        form = RecipeForm()

    context = {'form': form}
    return render(request, "create_recipe.html", context)

def delete_recipe(request, id):
    recipe = Recipe.objects.get(pk=id)
    recipe.delete()
    return HttpResponseRedirect(reverse('main'))

def verify_user(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_id)

    user.is_verified = True
    user.save()

    return redirect('user_list')