from django.db import models
from django.contrib.auth.models import User
from main.models import Recipe

# Create your models here.
class ReviewItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)

    def __str__(self):
        return self.recipe.name