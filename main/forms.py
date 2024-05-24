from django.forms import ModelForm

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "description", "ingredients", "directions", "nutrition_facts"]
    
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['description'].required = True
        self.fields['ingredients'].required = True
        self.fields['directions'].required = True
        self.fields['nutrition_facts'].required = True