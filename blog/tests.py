from django.test import TestCase
from django.urls import resolve
from .views import post_list

# Create your tests here.

class HomePageTest(TestCase):

	def test_root_goes_to_home_page(self):
		found = resolve('/')
		self.assertEqual(found.func, post_list)
