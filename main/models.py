from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    chef = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    nutrition_facts = models.TextField()