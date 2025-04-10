"""This file contains the test cases for the ocean_basket app."""
import unittest
from django.apps import apps
from .apps import OceanBasketConfig


class TestOceanBasketConfig(unittest.TestCase):
    """ This class contains test cases for the OceanBasketConfig class. """
    def test_app_config(self):
        """ Test the OceanBasketConfig class. """
        self.assertEqual(OceanBasketConfig.name, 'ocean_basket')
        self.assertEqual(
            apps.get_app_config('ocean_basket').name,
            'ocean_basket'
        )
