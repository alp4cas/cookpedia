from django.db import models
from django.contrib.auth.models import User
from main.models import Recipe

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    recipes = models.ManyToManyField(Recipe, related_name='collections', blank=True)

    def __str__(self):
        return self.name
