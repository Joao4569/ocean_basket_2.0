""" This file contains the test cases for the views in the
ocean_basket app. """
from django.test import TestCase
from django.contrib.auth.models import User


class TestHome(TestCase):
    """This test case checks the functionality of the home page."""
    def test_get_home_page(self):
        """Test the home page loads correctly."""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'online_booking/index.html')


class TestAllauthLogin(TestCase):
    """This test case checks the functionality of the login page."""

    def test_get_login_page(self):
        """Test the login page loads correctly."""
        # Simulate a GET request to the login page
        response = self.client.get('/accounts/login/')
        # Check the response status code and template used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_login_user(self):
        """Test logging in a user."""
        # Create a test user
        user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Simulate a login request
        response = self.client.post('/accounts/login/', {
            'login': user.username,
            'password': 'testpassword'
        })

        # Check the response and authentication
        # Check if the user is authenticated
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        # Expect a redirect after successful login
        self.assertEqual(response.status_code, 302)
        # Check if the user is redirected to the home page
        self.assertEqual(response['Location'], '/')


class TestAllauthSignUp(TestCase):
    """This test case checks the functionality of the Allauth Signup page."""

    def test_get_signup_page(self):
        """Test the signup page loads correctly."""
        # Simulate a GET request to the signup page
        response = self.client.get('/accounts/signup/')
        # Check the response status code and template used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_signup_user(self):
        """Test signing up a new user."""
        # Simulate a POST request to the signup page with valid data
        response = self.client.post('/accounts/signup/', {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123'
        })

        # Check if the user is created
        self.assertTrue(User.objects.filter(username='newuser').exists())
        # Expect a redirect after successful signup
        self.assertEqual(response.status_code, 302)
        # Check if the user is redirected to the home page
        self.assertEqual(response['Location'], '/')
