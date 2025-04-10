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

    # def test_invalid_email(self):
    #     """Test that the form is invalid with an improperly formatted email."""
    #     form = CustomSignupForm(data={
    #         'first_name': 'John',
    #         'last_name': 'Test',
    #         'email': 'invalid-email',
    #         'password1': 'strongpassword123',
    #         'password2': 'strongpassword123'
    #     })
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('email', form.errors.keys())

    # def test_passwords_do_not_match(self):
    #     """Test that the form is invalid when passwords do not match."""
    #     form = CustomSignupForm(data={
    #         'first_name': 'John',
    #         'last_name': 'Doe',
    #         'email': 'john.doe@example.com',
    #         'password1': 'strongpassword123',
    #         'password2': 'differentpassword123'
    #     })
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('password2', form.errors.keys())

    # def test_save_assigns_first_and_last_name(self):
    #     """Test that the save method assigns first_name and last_name."""
    #     form = CustomSignupForm(data={
    #         'email': 'john.test@example.com',
    #         'username': 'johntest',
    #         'first_name': 'John',
    #         'last_name': 'Test',
    #         'password1': 'strongpassword123',
    #         'password2': 'strongpassword123'
    #     })
    #     if form.is_valid():
    #         user = form.save(None)
    #         self.assertEqual(user.first_name, 'John')
    #         self.assertEqual(user.last_name, 'Test')

    # def test_save_handles_missing_first_name(self):
    #     """Test that the save method handles missing first_name."""
    #     form = CustomSignupForm(data={
    #         'email': 'john.test@example.com',
    #         'username': 'johntest',
    #         'first_name': '',
    #         'last_name': 'Test',
    #         'password1': 'strongpassword123',
    #         'password2': 'strongpassword123'
    #     })
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('first_name', form.errors.keys())

    # def test_save_handles_invalid_data(self):
    #     """Test that the save method handles invalid data."""
    #     form = CustomSignupForm(data={
    #         'email': 'invalid-email',
    #         'username': 'johntest',
    #         'first_name': 'John',
    #         'last_name': 'Test',
    #         'password1': 'strongpassword123',
    #         'password2': 'strongpassword123'
    #     })
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('email', form.errors.keys())

    # def test_save_handles_duplicate_email(self):
    #     """Test that the save method handles duplicate email."""
    #     # Create a user with the same email
    #     CustomSignupForm(data={
    #         'email': 'john.test@example.com',
    #         'username': 'johntest',
    #         'first_name': 'John',
    #         'last_name': 'Test',
    #         'password1': 'strongpassword123',
    #         'password2': 'strongpassword123'
    #     }).save(None)

        # Attempt to create another user with the same email
        # form = CustomSignupForm(data={
        #     'email': 'john.test@example.com',
        #     'username': 'janetest',
        #     'first_name': 'Jane',
        #     'last_name': 'Test',
        #     'password1': 'strongpassword123',
        #     'password2': 'strongpassword123'
        # })
        # self.assertFalse(form.is_valid())
        # self.assertIn('email', form.errors.keys())

    # def test_save_passwords_do_not_match(self):
    #     """Test that the save method handles mismatched passwords."""
    #     form = CustomSignupForm(data={
    #         'email': 'john.test@example.com',
    #         'username': 'johntest',
    #         'first_name': 'John',
    #         'last_name': 'Test',
    #         'password1': 'strongpassword123',
    #         'password2': 'differentpassword123'
    #     })
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('password2', form.errors.keys())
