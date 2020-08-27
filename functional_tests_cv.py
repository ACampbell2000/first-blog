from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest



class VisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def login(self):
		self.browser.get('http://localhost:8000')
		login = self.browser.find_element_by_id('login')
		login.click()

		usernameInput = self.browser.find_element_by_id('id_username')
		usernameInput.send_keys("ACampbell2000")

		passwordInput = self.browser.find_element_by_id('id_password')
		passwordInput.send_keys("tU9qnHsF9F68vTJ")
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

	#the user should open up the cv page and see 'Alex Campbell' printed in the right column with all of his details
	def test_right_column_shows_correct_details(self):
		self.browser.get('http://localhost:8000/cv/10/')
		self.assertIn('Alex', self.browser.title)
		header_text = self.browser.find_element_by_id('cv_title').text
		self.assertEquals('Alex Campbell', header_text)

		phoneNumber = self.browser.find_element_by_id('phone_number').text
		self.assertEquals('07757010372', phoneNumber)

		address = self.browser.find_element_by_id('address').text
		self.assertEquals('57 Chaffcombe Road, B26 3YA', address.strip())
		
		email = self.browser.find_element_by_id('email').text
		self.assertEquals('campbellalex02@gmail.com', email)


if __name__ == '__main__':
	unittest.main(warnings='ignore')