
from cmath import e
from pathlib2 import Path
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenarios, given, when, then
from pages.menuPageObj import menuPageObj



scenarios("menufeatures")
@given("I menu press the publish button")
def publish_article(browser):
    #try:
        menuPageObj(browser).searchinGoogle("https://www.amazon.in/")
        menuPageObj(browser).googleSearch()
    #except Exception:
        #browser.save_screenshot('.//output//screenshot.png')
        #print(Exception)
