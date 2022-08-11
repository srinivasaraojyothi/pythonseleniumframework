
from cmath import e
from pathlib2 import Path
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenarios, given, when, then
from pages.menuPageObj import menuPageObj
import logging
from logging import config

log_config_ini = "pytest.ini"
logging.config.fileConfig(log_config_ini)

logger = logging.getLogger()


scenarios("menufeatures")
@given("I menu press the publish button")
def publish_article(browser):
    #try:
        logger.critical('This outputs just to the scre')
        logger.debug("This does not write to either screen (expected) nor file (unexpected)")
        menuPageObj(browser).searchinGoogle("https://jqueryui.com/droppable/")
        menuPageObj(browser).edurekha()

    #except Exception:
        #browser.save_screenshot('.//output//screenshot.png')
        #print(Exception)
@given("navigate to google")        
def publish_article_1(browser):
    #try:
        logger.critical('This outputs just to the scre')
        logger.debug("This does not write to either screen (expected) nor file (unexpected)")
        menuPageObj(browser).searchinGoogle("https://www.google.com/")
@given("search in google")           
def googleSearch(browser):        
        menuPageObj(browser).searchText()