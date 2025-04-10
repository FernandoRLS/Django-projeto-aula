from django.test import TestCase

# Create your tests here.
# meu_app/tests.py
from django.test import TestCase
from django.urls import reverse

class SimpleViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Primeiro teste!")
