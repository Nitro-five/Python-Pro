# links/tests.py
from django.test import TestCase, Client
from .models import Link

class LinkTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.link = Link.objects.create(original_url="https://openweathermap.org/")

    def test_short_url_redirect(self):
        response = self.client.get(f"/{self.link.short_url}/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.link.original_url)

    def test_create_link(self):
        response = self.client.post("/", {"original_url": "https://openweathermap.org/guide"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Короткая ссылка")
