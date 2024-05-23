from django.forms import ModelForm
from main.models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "description", "ingredients", "directions", "nutrition_facts"]