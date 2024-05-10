from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe
from .utils import approve_recipe


class ApproveRecipeTestCase(TestCase):
    def setUp(self):
        self.admin = User.objects.create(username='admin', is_staff=True)
        self.recipe = Recipe.objects.create(title='Gourmet Negroni', is_approved=False)

    def test_approve_recipe(self):
        self.assertFalse(self.recipe.is_approved)

        approve_recipe(self.recipe)

        self.recipe.refresh_from_db()
        self.assertTrue(self.recipe.is_approved)

    def test_reject_recipe(self):
        self.assertFalse(self.recipe.is_approved)

        reject_recipe(self.recipe)

        self.recipe.refresh_from_db()
        self.assertFalse(self.recipe.is_approved)

class VerifyUserTestCase(TestCase):
    def setUp(self):
        self.admin = User.objects.create(username='admin', is_staff=True)
        self.user = User.objects.create(username='user', is_verified=False)

    def test_verify_user(self):
        self.assertFalse(self.user.is_verified)

        verify_user(self.user)

        self.user.refresh_from_db()
        self.assertTrue(self.user.is_verified)
