from django.test import TestCase


class TestDjango(TestCase):
    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ocean_basket/index.html')
