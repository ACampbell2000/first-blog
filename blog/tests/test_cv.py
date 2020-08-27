from django.test import TestCase
from blog.views import cv

class CVTest(TestCase):

	def test_cv_uses_correct_html(self):
		request = self.client.get('/cv/10/')
		self.assertTemplateUsed(request,'blog/cv.html')