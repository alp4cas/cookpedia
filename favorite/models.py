from django.db import models
from django.contrib.auth.models import User
from main.models import Recipe

class FavoriteItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe.name