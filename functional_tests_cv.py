from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import seed
from random import random
import time
import unittest



class VisitorTest(unittest.TestCase):

	#for the purposes of testing all of the fields have been filled with randomly generated numbers
	#such that each time the test is run is it almost guaranteed that each field will have a different
	#value, negating the possiblity of the test passing by fluke, i.e it says it has changed all
	#the fields and passes the test saying it has become the new values, but instead has not changed
	#them at all and still passed since the values were static.

	seed(1)

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
		#this is the password for the local database so it doesnt matter that it is in plain text here.
		passwordInput.submit()
		time.sleep(1)
		self.browser.back()
		self.browser.back()


	#if the user is logged in then they should be able to click on the name and edit the details of the cv, before saving again
	def test_can_change_cv_if_logged_in(self):
		VisitorTest.login(self)
		self.browser.get('http://localhost:8000/cv/')
		time.sleep(1)
		self.browser.find_element_by_id('cv_title').click()

		#the user edits their phone number which was recently changed
		input_phoneNumber = str(random()*1000)[:11]
		pn = self.browser.find_element_by_id('id_phone_number')
		pn.clear()
		pn.send_keys(input_phoneNumber)

		#they also edit their address after having moved recently
		input_address = str(random()*1000)
		ad = self.browser.find_element_by_id('id_address')
		ad.clear()
		ad.send_keys(input_address)

		#they change their email to one better suited for a CV
		input_email = str(random()*1000) + "@testing.com"
		em = self.browser.find_element_by_id('id_email')
		em.clear()
		em.send_keys(input_email)

		#they update their personal statement
		input_personalStatement = str(random()*1000)
		ps = self.browser.find_element_by_id('id_personal_statement')
		ps.clear()
		ps.send_keys(input_personalStatement)

		#they change their work experience after finding a typo
		input_workExperience = str(random()*1000)
		we = self.browser.find_element_by_id('id_work_experience')
		we.clear()
		we.send_keys(input_workExperience)

		input_projects = str(random()*1000)
		pr = self.browser.find_element_by_id('projects')
		pr.clear()
		pr.send_keys(input_projects)

		#finally they change one of their grades after mistaking one of their grades
		input_grades = str(random()*1000)
		gr = self.browser.find_element_by_id('id_grades')
		gr.clear()
		gr.send_keys(input_grades)

		#they then save their changes and are redirected back to the cv page to see how it looks
		self.browser.find_element_by_id('submit_button').click()
		title = self.browser.find_element_by_id('cv_title').text
		self.assertIn('Alex Campbell', title)

		#they see that all of their changes can be seen on the page
		phoneNumber = self.browser.find_element_by_id('phone_number').text
		self.assertEquals(phoneNumber, input_phoneNumber)

		address = self.browser.find_element_by_id('address').text
		self.assertEquals(address, input_address)

		email = self.browser.find_element_by_id('email').text
		self.assertEquals(email, input_email)

		personalStatement = self.browser.find_element_by_id('personal_statement').text
		self.assertEquals(personalStatement, input_personalStatement)

		workExperience = self.browser.find_element_by_id('work_experience').text
		self.assertEquals(workExperience, input_workExperience)

		projects = self.browser.find_element_by_id('projects').text
		self.assertEquals(projects,input_projects)

		grades = self.browser.find_element_by_id('grades').text
		self.assertEquals(grades, input_grades)


if __name__ == '__main__':
	unittest.main(warnings='ignore')