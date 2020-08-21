from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import post_list

# Create your tests here.

class HomePageTest(TestCase):

	def test_root_goes_to_home_page(self):
		found = resolve('/')
		self.assertEqual(found.func, post_list)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = post_list(request)
		html = response.content.decode('utf8')
		#it is new line first since the first line is actually {% load static %} but this appears as an empty line in html
		self.assertTrue(html.startswith('\n<html>'))
		self.assertIn('<title>Alex\'s Blog</title>', html)
		self.assertTrue(html.endswith('</html>'))
