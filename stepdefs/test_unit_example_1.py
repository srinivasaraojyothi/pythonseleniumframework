import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.errorhandler import ErrorHandler
from pages.menuPageObj import menuPageObj
from pyallied.api_crud import crud
#from HtmlTestRunner import HTMLTestRunner
import HtmlTestRunner
import logging
from logging import config
import pytest
log_config_ini = "pytest.ini"
logging.config.fileConfig(log_config_ini)

logger = logging.getLogger()

class SampleCase_2(unittest.TestCase):

    def setUp(self):
            opts = webdriver.ChromeOptions()

            opts.add_argument('--disable-gpu')
            
            self.browser = webdriver.Chrome("D:/Users/sjyothi/Downloads/chromedriver/chromedriver.exe", options=opts)
    @pytest.mark.tt
    def test_method_1(self):
        menuPageObj(self.browser).searchinGoogle("https://www.amazon.in/")
        menuPageObj(self.browser).googleSearch()

    def tearDown(self):
        # clean up code
        self.browser.quit()


if __name__ == "__main__":
    #testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports")
    unittest.main()