"""  This module contains test cases for the custom signup form. """
from django.test import TestCase
from .forms import CustomSignupForm


class TestCustomSignupForm(TestCase):
    """ This test case checks the functionality of the custom signup form. """
    def test_first_name_is_required(self):
        """  Test that first name is required. """
        form = CustomSignupForm(data={'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'], ['This field is required.']
        )

    def test_last_name_is_required(self):
        """  Test that last name is required. """
        form = CustomSignupForm(data={'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(
            form.errors['last_name'], ['This field is required.']
        )

    def test_form_is_valid_with_all_fields(self):
        """Test that the form is valid when all required fields are
        provided."""
        form = CustomSignupForm(data={
            'email': 'johntest@example.com',
            'username': 'johntest',
            'first_name': 'John',
            'last_name': 'Test',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123'
        })
        self.assertTrue(form.is_valid())

    def test_first_name_max_length(self):
        """Test that first name does not exceed max length."""
        form = CustomSignupForm(data={'first_name': 'A' * 26})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())

    def test_last_name_max_length(self):
        """Test that last name does not exceed max length."""
        form = CustomSignupForm(data={'last_name': 'B' * 26})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
