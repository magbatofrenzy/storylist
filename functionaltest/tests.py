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
		
		inputgender = self.browser.find_element_by_id ('Cgname')
		self.assertEqual(inputgender.get_attribute ('placeholder'),'Write Here!')
		inputgender.click()
		time.sleep(1)
		inputgender.send_keys ('Female')
		time.sleep(1)

		inputreader = self.browser.find_element_by_id('rname')
		self.assertEqual(inputreader.get_attribute('placeholder'),'Fill Here')
		inputreader.click()
		time.sleep(1)
		inputreader.send_keys('Frenzy Camille Magbato')
		time.sleep(1)

		inputcategory= self.browser.find_element_by_id('ncategory')
		self.assertEqual(inputcategory.get_attribute('placeholder'),'Fill Title Here')
		inputcategory.click()
		time.sleep(1)
		inputcategory.send_keys('FairyTale')
		time.sleep(1)

		inputtitle = self.browser.find_element_by_id('ntitle')
		self.assertEqual(inputtitle.get_attribute('placeholder'),'Enter Title Here')
		inputtitle.click()
		time.sleep(1)
		inputtitle.send_keys('Snow White and the Seven Dwarfs')
		time.sleep(1)

		inputauthor = self.browser.find_element_by_id('nauthor')
		self.assertEqual(inputauthor.get_attribute('placeholder'), 'Writers Name')
		inputauthor.click()
		time.sleep(1)
		inputauthor.send_keys('Jacob Grimm')
		time.sleep(1)

		btnEnter = self.browser.find_element_by_id('btnEnter')
		btnEnter.click()
		time.sleep(2)

		inputsynopsis = self.browser.find_element_by_id('nsynopsis')
		self.assertEqual(inputsynopsis.get_attribute('placeholder'),'Summary')
		inputsynopsis.click()
		time.sleep(1)
		inputsynopsis.send_keys('They lived happily ever after!')
		time.sleep(1)

		btnEnter = self.browser.find_element_by_id('btnEnter')
		btnEnter.click()
		time.sleep(2)



	



