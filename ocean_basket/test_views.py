""" This file contains the test cases for the views in the
ocean_basket app. """
from django.test import TestCase
from django.contrib.auth.models import User
from .models import BookingInformation  # Import the BookingInformation model


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


class TestViewBookings(TestCase):
    """This test case checks the functionality of the view_bookings page."""
    def test_get_view_bookings_page(self):
        """Test the view_bookings page loads correctly."""
        response = self.client.get('/view_bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'online_booking/view_bookings.html')


class TestViewBookingsEmployee(TestCase):
    """This test case checks the functionality of the view_bookings page for
    an employee of Ocean Basket."""
    def test_get_view_bookings_employee_page(self):
        """Test the view_bookings_employee page loads correctly."""
        response = self.client.get('/view_bookings_employee/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'online_booking/view_bookings.html'
        )


class CreateBooking(TestCase):
    """This test case checks the functionality of the create_booking page."""
    def test_get_create_booking_page(self):
        """Test the create_booking page loads correctly."""
        response = self.client.get('/create_booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'online_booking/create_booking.html')


class TestEditBooking(TestCase):
    """This test case checks the functionality of the edit_booking page."""

    def setUp(self):
        """Set up a test booking instance."""
        # pylint: disable=no-member
        self.booking = BookingInformation.objects.create(
            username="testuser",
            booking_title="Birthday Party",
            service=BookingInformation.LUNCH,
            number_of_seats=4,
            date="2023-10-01",
            contact_number="1234567890"
        )

    def test_get_edit_booking_page(self):
        """Test the edit_booking page loads correctly."""
        response = self.client.get(f'/edit_booking/{self.booking.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'online_booking/edit_booking.html')


class TestDeleteBooking(TestCase):
    """This test case checks the functionality of the delete_booking page."""

    def setUp(self):
        """Set up a test booking instance."""
        # pylint: disable=no-member
        self.booking = BookingInformation.objects.create(
            username="testuser",
            booking_title="Meeting",
            service=BookingInformation.DINNER,
            number_of_seats=2,
            date="2023-11-01",
            contact_number="9876543210"
        )

    def test_delete_booking(self):
        """Test deleting a booking."""
        response = self.client.post(f'/delete_booking/{self.booking.id}/')
        # Check if the booking is deleted
        # pylint: disable=no-member
        self.assertFalse(
            BookingInformation.objects.filter(id=self.booking.id).exists()
        )
        # Expect a redirect after successful deletion
        self.assertEqual(response.status_code, 302)
        # Check if the user is redirected to the view bookings page
        self.assertEqual(response['Location'], '/view_bookings/')
