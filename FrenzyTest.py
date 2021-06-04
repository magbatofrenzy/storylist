from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class PageTest(unittest.TestCase):
	def setUp(self):
	    self.browser = webdriver.Firefox()

	def test_browser_title(self):
	    self.browser.get('http://localhost:8000/')
	    self.assertIn('Story Registration List',self.browser.title)


	def check_for_rows_in_list_table(self,row_text):
	    table = self.browser.find_element_by_id('listTable')
	    rows = table.find_elements_by_tag_name('tr')
	    self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_and_retrieve_it(self):
	    self.browser.get('http://localhost:8000/')
	    self.assertIn("Story Registration List",self.browser.title)

	    header_Text = self.browser.find_element_by_tag_name('h1')
	    self.assertIn("Story Registration List", header_Text)
	 
	 
	    
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class PageTest(unittest.TestCase):
	def setUp(self):
	    self.browser = webdriver.Firefox()

	def test_browser_title(self):
	    self.browser.get('http://localhost:8000/')
	    self.assertIn("Story Registration ListS",self.browser.title)

	def check_for_rows_in_list_table(self,row_text):
	    table = self.browser.find_element_by_id('listTable')
	    rows = table.find_elements_by_tag_name('tr')
	    self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_and_retrieve_it(self):
	    self.browser.get('http://localhost:8000/')
	    self.assertIn("Story Registration List",self.browser.title)

	    header_Text = self.browser.find_element_by_tag_name('h1')
	    self.assertIn("Story Registration List", header_Text)
		 
		inputgender = self.browser.find_element_by_id ('gender')
		self.assertEqual(inputgender,get_attribute ('placeholder'), 'Write Here!')
		inputgender.click()
		time.sleep(1)
		inputgender.send_keys ('Female')
		time.sleep(1)

		inputreader = self.browser.find_element_by_id('reader')
		self.assertEqual(inputreader.get_attribute('placeholder'),'Fill Here')
	 	inputreader.click()
	 	time.sleep(1)
	 	inputreader.send_keys('Frenzy Camille Magbato')
	 	time.sleep(1)
	 
	 	inputcategory= self.browser.find_element_by_id('category')
	 	self.assertEqual(inputcategory.get_attribute('placeholder'),'Fill Title Here')
	 	inputcategory.click()
	 	time.sleep(1)
	 	inputcategory.send_keys('FairyTale')
	 	time.sleep(1)
	 
	 	inputtitle = self.browser.find_element_by_id('title')
	 	self.assertEqual(inputtitle.get_attribute('placeholder'),'Enter Title Here')
	 	inputtitle.click()
	 	time.sleep(1)
	 	inputtitle.send_keys('Snow White and the Seven Dwarfs')
	 	time.sleep(1)
	 
	 	inputauthor = self.browser.find_element_by_id('author')
	 	self.assertEqual(inputauthor.get_attribute('placeholder'), 'Writers Name')
	 	inputauthor.click()
	 	time.sleep(1)
	 	inputauthor.send_keys('Jacob Grimm')
	 	time.sleep(1)
	 
	 	inputsypnosis = self.browser.find_element_by_id('sypnosis')
	 	self.assertEqual(inputsypnosis.get_attribute('placeholder'),'Summary')
	 	inputsypnosis.click()
	 	time.sleep(1)
	 	inputsypnosis.send_keys('They lived happily ever after!')
	 	time.sleep(1)

		btnContinue = self.browser.find_element_by_tag_name('btnContinue')
		btnContinue.click()
		time.sleep(2)
	 
