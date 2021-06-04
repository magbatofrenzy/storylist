from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class PageTest(LiveServerTestCase):

	def wait_for_table(self, row_text):        
		start_time = time.time()
		while True:  
			try:
				table = self.browser.find_element_by_id('listTable')                  
				rows = table.find_elements_by_tag_name('tr')                
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:  
				if time.time() - start_time > MAX_WAIT:  
					raise e                  
					time.sleep(0.5)  

	
	def setUp(self):
		self.browser = webdriver.Firefox()


	def test_browser_title(self):
		self.browser.get('http://localhost:8000/')
		#self.browser.get(self.live_server_url)
		self.assertIn('Story Registration List',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Story Registration List', header_text)
		
		inputbox1 = self.browser.find_element_by_id('rname')
		self.assertEqual(inputbox1.get_attribute('placeholder'),'Write Here!')
		inputbox1.send_keys('Frenzy Magbato')
		time.sleep(1)

		inputbox2 = self.browser.find_element_by_id('Gender')
		self.assertEqual(inputbox2.get_attribute('placeholder'),'F/M')
		inputbox2.send_keys('Female')
		time.sleep(1)


		btnSubmit = self.browser.find_element_by_id('btnEnter')
		btnSubmit.click()
		time.sleep(2)

	



