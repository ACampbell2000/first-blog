from django.test import TestCase
from blog.views import post_list
from django.contrib.auth.models import User
from blog.models import CV

# Create your tests here.

class CVTest(TestCase):

	password = "test"

	def setUp(self):
		self.user = User.objects.create_user(username='test', email='test@testing.com', password=CVTest.password)
		user = User.objects.first()

	def test_cv_returns_error_page_when_no_cv_exists(self):
		request = self.client.get('/cv/', follow=True)
		self.assertTemplateUsed(request, 'blog/error.html')

	def test_returns_cv_correctly(self):
		CV.objects.create(author=self.user, email=self.user.email)
		cv = CV.objects.first()
		self.assertEquals(cv.author, self.user)
		self.assertEquals(cv.email, self.user.email)

	def test_cv_page_returns_cv_template_when_one_exists(self):
		CV.objects.create(author=self.user, email=self.user.email)
		request = self.client.get('/cv/', follow=True)
		self.assertTemplateUsed(request, 'blog/cv.html')

	def test_cv_page_has_correct_details(self):
		CV.objects.create(author=self.user, email=self.user.email)
		request = self.client.get('/cv/', follow=True)
		self.assertContains(request, self.user.username)
		self.assertContains(request, self.user.email)
