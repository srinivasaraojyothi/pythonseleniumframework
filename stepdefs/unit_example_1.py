import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.errorhandler import ErrorHandler
from pages.menuPageObj import menuPageObj
#from HtmlTestRunner import HTMLTestRunner
import HtmlTestRunner

class SampleCase_2(unittest.TestCase):

    def setUp(self):
            opts = webdriver.ChromeOptions()

            opts.add_argument('--disable-gpu')
            
            self.browser = webdriver.Chrome("D:/Users/sjyothi/Downloads/chromedriver/chromedriver.exe", options=opts)

    def test_method_1(self):
        menuPageObj(self.browser).searchinGoogle("https://www.amazon.in/")
        menuPageObj(self.browser).googleSearch()

    def tearDown(self):
        # clean up code
        self.browser.quit()


if __name__ == "__main__":
    #testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports")
    unittest.main()