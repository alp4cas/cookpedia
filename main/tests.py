from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe
from .utils import approve_recipe

class VerifyUserTestCase(TestCase):
    def setUp(self):
        self.admin = User.objects.create(username='admin', is_staff=True)
        self.user = User.objects.create(username='user', is_verified=False)

    def test_verify_user(self):
        self.assertFalse(self.user.is_verified)

        verify_user(self.user)

        self.user.refresh_from_db()
        self.assertTrue(self.user.is_verified)