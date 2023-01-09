"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """
    Test models.
    """
    def test_create_user_with_email_successful(self):
        """
        Test creating a user with an email is successful
        :return:
        """
        email = 'test@example.com'
        password = 'testpassword'

        test_user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(test_user.email, email)
        self.assertTrue(test_user.check_password(password))



