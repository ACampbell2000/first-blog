from selenium import webdriver
import unittest


class VisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		# loading the local website assuming the server is running
		self.browser.quit()
	
	def test_open_website_with_correct_name(self):
		#checking Alex is in the title which should be Alex's blog
		self.browser.get('http://localhost:8000')
		self.assertIn('Alex', self.browser.title)
		self.fail('Finish')

if __name__ == '__main__':
	unittest.main(warnings='ignore')