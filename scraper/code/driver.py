# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Displays large datasets?
import pandas as pd
# Colors terminal text
import colorama
# Accessing website for crawling
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

from xvfbwrapper import Xvfb
from general_scraper import *

class Driver():
	def __init__(self):
		pass

	
	#XXX new init_driver func, headless
	@staticmethod
	def get_driver():
		vdisplay = Xvfb(width=1280, height=720)
		vdisplay.start()
		dr = webdriver.Firefox()
		dr.wait = WebDriverWait(dr, 5)
		# Wait is so that slow JS websites will load
		WebDriverWait(dr, 10)
		dr.set_page_load_timeout(25)
		return dr

	@staticmethod
	def teardown_driver(dr):
		close_msg = 'Closing driver'
		log_time('info', msg=close_msg)
		# Closes all pages and ends selenium processes gracefully
		dr.quit()

# DEPRECATED: has head
#	def get_driver(self, driver_type='Firefox'):
#		if driver_type.startswith('Chr'):
#			dr = webdriver.Chrome()
#		elif driver_type.startswith('Pha'):
#			dr = webdriver.PhantomJS()
#		elif driver_type.startswith('Fi'):
#			dr = webdriver.Firefox()
#		else:
#			assert False
#		return dr
	
# DEPRECATED: used for setting up -- window size etc -- 
# but not starting browser

#	def setup_driver(self, dr, driver_type):
#		log_time('info')
#		print('initiating dr: {}'.format(driver_type))
#		dr.set_window_size(1920, 600)
#		dr.wait = WebDriverWait(dr, 5)
#		dr.set_page_load_timeout(25)
#		return dr

