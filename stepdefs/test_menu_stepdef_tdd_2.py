
from cmath import e
from pathlib2 import Path
import pytest
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenarios, given, when, then
from pages.menuPageObj import menuPageObj
import logging
from logging import config

log_config_ini = "pytest.ini"
logging.config.fileConfig(log_config_ini)

logger = logging.getLogger()



@pytest.mark.slow
def test_publish_article_4(browser):
        #try:
            menuPageObj(browser).searchinGoogle("https://www.amazon.in/")
            menuPageObj(browser).googleSearch()
            logger.critical('This outputs just to the scre_critical')
            logger.info("This does not write to either screen (expected) nor file (unexpected)_info") 
            logger.debug("debug")  
            logger.exception("exception----")  
        #except Exception:
            #browser.save_screenshot('.//output//screenshot.png')
            #print(Exception)

@pytest.mark.slow
def test_publish_article__5(browser):
        #try:
            menuPageObj(browser).searchinGoogle("https://www.amazon.in/")
            menuPageObj(browser).googleSearch()
        #except Exception:
            #browser.save_screenshot('.//output//screenshot.png')
            #print(Exception)

@pytest.mark.slow
def test_publish_article_6(browser):
        #try:
            menuPageObj(browser).searchinGoogle("https://www.amazon.in/")
            menuPageObj(browser).googleSearch()
        #except Exception:
            #browser.save_screenshot('.//output//screenshot.png')
            #print(Exception)
