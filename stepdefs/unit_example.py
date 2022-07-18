import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.errorhandler import ErrorHandler
from pages.menuPageObj import menuPageObj
from pyallied.web.keys import Keys
#from HtmlTestRunner import HTMLTestRunner
import HtmlTestRunner

class SampleCase(unittest.TestCase):

    def setUp(self):
            opts = webdriver.ChromeOptions()

            opts.add_argument('--disable-gpu')
            
            self.browser = webdriver.Chrome("D:/Users/sjyothi/Downloads/chromedriver/chromedriver.exe", options=opts)

    def test_method(self):
        menuPageObj(self.browser).searchinGoogle("https://www.amazon.in/")
        menuPageObj(self.browser).googleSearch()

    def tearDown(self):
        # clean up code
        self.browser.quit()



#if __name__ == "__main__":
    #testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports")
    #unittest.main()