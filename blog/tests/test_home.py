from django.test import TestCase

from blog.views import post_list

# Create your tests here.

class HomePageTest(TestCase):

	def test_home_page_returns_correct_html(self):
		request = self.client.get('/')
		self.assertTemplateUsed(request, 'blog/post_list.html')
