from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    nutrition_facts = models.TextField()
    status = models.CharField(max_length=50, default='PENDING')