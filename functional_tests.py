from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import seed
from random import random
import time
import unittest


class VisitorTest(unittest.TestCase):

	seed(1)

	postTitleTest = "selenium test title " + str(random()*1000)
	postTextTest = "selenium test text " + str(random()*1000)

	draftTitleTest = "selenium draft test title " + str(random()*1000)
	draftTextTest = "selenium draft test text " + str(random()*1000)

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_open_website_with_correct_name_and_title(self):
		#checking Alex is in the title which should be Alex's blog
		self.browser.get('http://localhost:8000')
		self.assertIn('Alex', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Alex\'s Blog', header_text)

	def login(self):
		self.browser.get('http://localhost:8000')
		login = self.browser.find_element_by_id('login')
		login.click()

		usernameInput = self.browser.find_element_by_id('id_username')
		usernameInput.send_keys("ACampbell2000")

		passwordInput = self.browser.find_element_by_id('id_password')
		passwordInput.send_keys("tU9qnHsF9F68vTJ")
		#this is the password for the local database so it doesnt matter that it is in plain text here.
		passwordInput.submit()
		time.sleep(1)
		self.browser.back()
		self.browser.back()


	def test_delete_draft(self):
		self.browser.get('http://localhost:8000')
		VisitorTest.login(self)
		self.browser.find_element_by_id('post_draft_list').click()

		posts = self.browser.find_elements_by_class_name('post')

		for post in posts:
			if (post.find_element_by_class_name('post-title').text == (VisitorTest.draftTitleTest + "1") and post.find_element_by_class_name('post-text').text == (VisitorTest.draftTextTest + "1")):
				post.find_element_by_class_name('post-title').click()
				break

		time.sleep(1)
		self.browser.find_element_by_class_name('post').find_element_by_id('delete_button').click()
		time.sleep(1)

		self.browser.find_element_by_id('post_draft_list').click()

		posts = self.browser.find_elements_by_class_name('post')

		self.assertFalse(
			any((post.find_element_by_class_name('post-title').text == (VisitorTest.draftTitleTest + "1") and
				post.find_element_by_class_name('post-text').text == (VisitorTest.draftTextTest + "1")) for post in posts)
			)

	def test_add_post_to_drafts_and_edit(self):
		self.browser.get('http://localhost:8000')
		VisitorTest.login(self)
		newPost = self.browser.find_element_by_id('add_post')
		newPost.click()

		inputTitleBox = self.browser.find_element_by_id('id_title')
		inputTitleBox.send_keys(VisitorTest.draftTitleTest)
		inputTextBox = self.browser.find_element_by_id('id_text')
		inputTextBox.send_keys(VisitorTest.draftTextTest)
		submitButton = self.browser.find_element_by_id('submit_button')
		submitButton.click()


		posts = self.browser.find_elements_by_class_name('post')
		self.assertTrue(
			any((post.find_element_by_class_name('post-title').text == VisitorTest.draftTitleTest and
				post.find_element_by_class_name('post-text').text == VisitorTest.draftTextTest) for post in posts)
			)

		for post in posts:
			if (post.find_element_by_class_name('post-title').text == VisitorTest.draftTitleTest and post.find_element_by_class_name('post-text').text == VisitorTest.draftTextTest):
				post.find_element_by_class_name('post-title').click()
				break

		time.sleep(1)
		self.browser.find_element_by_class_name('post').find_element_by_id('edit_button').click()
		time.sleep(1)

		inputTitleBox = self.browser.find_element_by_id('id_title')
		inputTitleBox.clear()
		inputTitleBox.send_keys(VisitorTest.draftTitleTest + "1")

		inputTextBox = self.browser.find_element_by_id('id_text')
		inputTextBox.clear()
		inputTextBox.send_keys(VisitorTest.draftTextTest + "1")

		submitButton = self.browser.find_element_by_id('submit_button')
		submitButton.click()

		posts = self.browser.find_elements_by_class_name('post')
		self.assertTrue(
			any((post.find_element_by_class_name('post-title').text == (VisitorTest.draftTitleTest + "1") and
				post.find_element_by_class_name('post-text').text == (VisitorTest.draftTextTest + "1")) for post in posts)
			)

	def test_delete_published_post(self):
		self.browser.get('http://localhost:8000')
		VisitorTest.login(self)
		posts = self.browser.find_elements_by_class_name('post')

		for post in posts:
			if (post.find_element_by_class_name('post-title').text == (VisitorTest.postTitleTest + "1") and post.find_element_by_class_name('post-text').text == (VisitorTest.postTextTest + "1")):
				post.find_element_by_class_name('post-title').click()
				break

		time.sleep(1)
		self.browser.find_element_by_class_name('post').find_element_by_id('delete_button').click()
		time.sleep(1)

		posts = self.browser.find_elements_by_class_name('post')

		self.assertFalse(
			any((post.find_element_by_class_name('post-title').text == (VisitorTest.postTitleTest + "1") and
				post.find_element_by_class_name('post-text').text == (VisitorTest.postTextTest + "1")) for post in posts)
			)


	def test_add_post_to_blog_and_edit(self):
		self.browser.get('http://localhost:8000')
		VisitorTest.login(self)
		newPost = self.browser.find_element_by_id('add_post')
		newPost.click()

		inputTitleBox = self.browser.find_element_by_id('id_title')
		inputTitleBox.send_keys(VisitorTest.postTitleTest)
		inputTextBox = self.browser.find_element_by_id('id_text')
		inputTextBox.send_keys(VisitorTest.postTextTest)
		submitButton = self.browser.find_element_by_id('submit_button')
		submitButton.click()

		self.browser.find_element_by_class_name('post').find_element_by_id('publish_button').click()
		self.browser.find_element_by_id('home_button').click()

		posts = self.browser.find_elements_by_class_name('post')
		self.assertTrue(
			any((post.find_element_by_class_name('post-title').text == VisitorTest.postTitleTest and
				post.find_element_by_class_name('post-text').text == VisitorTest.postTextTest) for post in posts)
			)

		for post in posts:
			if (post.find_element_by_class_name('post-title').text == VisitorTest.postTitleTest and post.find_element_by_class_name('post-text').text == VisitorTest.postTextTest):
				post.find_element_by_class_name('post-title').click()
				break

		time.sleep(1)
		self.browser.find_element_by_class_name('post').find_element_by_id('edit_button').click()
		time.sleep(1)

		inputTitleBox = self.browser.find_element_by_id('id_title')
		inputTitleBox.clear()
		inputTitleBox.send_keys(VisitorTest.postTitleTest + "1")

		inputTextBox = self.browser.find_element_by_id('id_text')
		inputTextBox.clear()
		inputTextBox.send_keys(VisitorTest.postTextTest + "1")

		submitButton = self.browser.find_element_by_id('submit_button')
		submitButton.click()

		posts = self.browser.find_elements_by_class_name('post')
		self.assertTrue(
			any((post.find_element_by_class_name('post-title').text == (VisitorTest.postTitleTest + "1") and
				post.find_element_by_class_name('post-text').text == (VisitorTest.postTextTest + "1")) for post in posts)
			)
			
if __name__ == '__main__':
	unittest.main(warnings='ignore')