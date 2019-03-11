from django.test import TestCase
from django.urls import resolve
from .views import home_page

class HomgePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)