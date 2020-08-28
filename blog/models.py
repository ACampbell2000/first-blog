from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title


class CV(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=11, default = "Enter")
	address = models.CharField(max_length=200, default="Enter Address")
	email = models.EmailField(default="enter@email.com")
	personal_statement = models.TextField(default="Enter Personal Statement")
	work_experience = models.TextField(default="Enter Work Experience")
	grades = models.TextField(default="Enter Grades")


	def publish(self):
		self.save()