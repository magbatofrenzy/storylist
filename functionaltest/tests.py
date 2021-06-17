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

		inputbox3 = self.browser.find_element_by_id('Category')
		self.assertEqual(inputbox3.get_attribute('placeholder'), 'Type Here')
		inputbox3.send_keys('Fairytale')
		time.sleep(1)

		inputbox4 =self.browser.find_element_by_id('reader')
		self.assertEqual(inputbox4.get_attribute('placeholder'),'Right Here')
		inputbox4.send_keys('Carolyn Quillope')
		time.sleep(1)

		inputbox5 =self.browser.find_element_by_id('Stories')
		self.assertEqual(inputbox5.get_attribute('placeholder'),'Type Here')
		inputbox5.send_keys('Treetop Family')
		time.sleep(1)

		inputbox6 =self.browser.find_element_by_id('Author')
		self.assertEqual(inputbox6.get_attribute('placeholder'),'Aname')
		inputbox6.send_keys('Nicholas Monsarrat')
		time.sleep(1)

		inputbox7 =self.browser.find_element_by_id('category')
		self.assertEqual(inputbox7.get_attribute('placeholder'),'Fill here!')
		inputbox7.send_keys('ADVENTURE')
		time.sleep(1)

		inputbox8 =self.browser.find_element_by_id('List')
		self.assertEqual(inputbox8.get_attribute('placeholder'),'Write Here')
		inputbox8.send_keys('Carolyn Quillope')
		time.sleep(1)

		inputbox9 =self.browser.find_element_by_id('Condition')
		self.assertEqual(inputbox9.get_attribute('placeholder'),'Fill Here!')
		inputbox9.send_keys('new reader')
		time.sleep(1)

		inputbox10 =self.browser.find_element_by_id('Remarks')
		self.assertEqual(inputbox10.get_attribute('placeholder'),'Record Here')
		inputbox10.send_keys('unfinised')
		time.sleep(1)

		btnSubmit = self.browser.find_element_by_id('btnEnter')
		btnSubmit.click()
		time.sleep(2)

	



