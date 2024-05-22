from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import RecipeForm
from .models import Recipe

def home(request):
    return render(request, 'homepage.html')

def main(request):
    recipes = Recipe.objects.all()
    return render(request, 'main.html', {'recipes': recipes})

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
