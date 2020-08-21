from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class VisitorTest(unittest.TestCase):


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
		passwordInput.send_keys("SOphieC070")
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		# THIS NEEDS TO BE REMOVED BEFORE HANDING IN
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		passwordInput.submit()
		time.sleep(1)
		self.browser.back()
		self.browser.back()


	def test_add_post_to_drafts(self):
		self.browser.get('http://localhost:8000')
		VisitorTest.login(self)
		newPost = self.browser.find_element_by_id('add_post')
		newPost.click()

		titleTest = "selenium test title"
		textTest = "selenium test text"

		inputTitleBox = self.browser.find_element_by_id('id_title')
		inputTitleBox.send_keys(titleTest)
		inputTextBox = self.browser.find_element_by_id('id_text')
		inputTextBox.send_keys(textTest)
		submitButton = self.browser.find_element_by_id('submit_button')
		submitButton.click()
		time.sleep(3)

		posts = self.browser.find_elements_by_class_name('post')
		self.assertTrue(
			any((post.find_element_by_class_name('post-title').text == titleTest and
				post.find_element_by_class_name('post-text').text == textTest) for post in posts)
			)


if __name__ == '__main__':
	unittest.main(warnings='ignore')