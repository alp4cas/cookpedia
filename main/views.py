from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .models import *

from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from main.forms import *

from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required

@login_required(login_url='auth/login')
def home(request):
    return render(request, 'homepage.html')

def manage_recipe(request):
    return render(request, 'manage_recipe.html')

def manage_user(request):
    return render(request, 'verify_user.html')

def get_user(request):
    User = get_user_model()
    data = User.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_recipe(request, param):
    data = Recipe.objects.filter(status=param)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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
            return HttpResponseRedirect(reverse('main:recipe_list'))  
        else:
            # If the form is not valid, re-render the page with the form containing error messages
            context = {'form': form}
            return render(request, "create_recipe.html", context)
    else:
        form = RecipeForm()

    context = {'form': form}
    return render(request, "create_recipe.html", context)

def delete_recipe(request, id):
    recipe = Recipe.objects.get(pk=id)
    recipe.delete()
    return HttpResponseRedirect(reverse('main:recipe_list'))

def set_recipe_status(request, recipe_id, status):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    recipe.status = status
    recipe.save()
    return redirect('main:manage_recipe')

def show_recipe(request):
    data = Recipe.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def verify_user(request, user_id, status):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_id)

    user.status = status
    user.save()

    return redirect('main:manage_user')