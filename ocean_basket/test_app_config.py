""" This file contains the test cases for the app configuration of
the Ocean Basket app. """
from django.apps import apps
from django.test import TestCase
from ocean_basket.apps import OceanBasketConfig


class TestOceanBasketConfig(TestCase):
    """Test the OceanBasket app configuration."""
    def test_app_config(self):
        """ Verify the app configuration is correctly set up. """
        self.assertEqual(OceanBasketConfig.name, 'ocean_basket')
        self.assertEqual(
            apps.get_app_config('ocean_basket').name,
            'ocean_basket'
        )
