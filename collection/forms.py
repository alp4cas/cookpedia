from django import forms
from .models import Collection
from main.models import Recipe


class CollectionForm(forms.ModelForm):
    recipes = forms.ModelMultipleChoiceField(
        queryset=Recipe.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        self.fields['recipes'].label_from_instance = self.label_from_recipe

    def label_from_recipe(self, obj):
        # Customize the display format here
        return f"{obj.name} - {obj.ingredients[:50]}..."  # Example format

    class Meta:
        model = Collection
        fields = ['name', 'description', 'recipes']
