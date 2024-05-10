from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from main.forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

@login_required(login_url='user_auth:login')
def home(request):
    return render(request, 'homepage.html')

def manage_recipe(request):
    return render(request, 'manage_recipe.html')
    
def main(request):
    return render(request, 'main.html')

def get_recipe(request, param):
    data = Recipe.objects.filter(status=param)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='user_auth:login')
def recipe_list(request):
    # recipes = Recipe.objects.all()
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipe_list.html', {'recipes': recipes})

def create_recipe(request):  
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('main:recipe_list'))  
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

def verify_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.user.role != "ADMIN":
        return render(request, 'error.html', {'message': 'You are not authorized to approve recipes.'})

    user.is_verified = True
    user.save()

    return redirect('user_list')