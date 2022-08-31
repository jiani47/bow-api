from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):


    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password (password))

    def test_create_superuser_with_email_successful(self):
        email = 'staff@example.com'
        password = 'staff'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)