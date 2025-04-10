""" This file contains the test cases for the views in the
ocean_basket app. """
from django.test import TestCase


class TestHome(TestCase):
    """This test case checks the functionality of the home page."""
    def test_get_home_page(self):
        """Test the home page loads correctly."""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'online_booking/index.html')
