from django.apps import apps
from django.test import TestCase
from ocean_basket.apps import OceanBasketConfig


class TestOceanBasketConfig(TestCase):
    def test_app_config(self):
        # Verify the app configuration is correctly set
        self.assertEqual(OceanBasketConfig.name, 'ocean_basket')
        self.assertEqual(
            apps.get_app_config('ocean_basket').name,
            'ocean_basket'
        )
