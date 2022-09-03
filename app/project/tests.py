from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models as core_models
from project import models as project_models

# Create your tests here.
class TestProjectApi(TestCase):
    def test_project_creation_successful(self):
        user = get_user_model().objects.create_user('test@example.com', 'password123')
      