from django.db import models
from django.contrib.auth.models import User as BaseUser

class Recipe(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    nutrition_facts = models.TextField()
    status = models.CharField(max_length=50, default='PENDING')

class User(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    username = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    role = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, default='UNVERIFIED')