
from cmath import e
from pathlib2 import Path
import pytest
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenarios, given, when, then
from pages.menuPageObj import menuPageObj




@pytest.mark.slow
def test_publish_article(browser):
        #try:
            menuPageObj(browser).searchinGoogle("https://www.amazon.in/")
            menuPageObj(browser).googleSearch()
        #except Exception:
            #browser.save_screenshot('.//output//screenshot.png')
            #print(Exception)

@pytest.mark.slow
def test_publish_article_2(browser):
        #try:
            menuPageObj(browser).searchinGoogle("https://www.amazon.in/")
            menuPageObj(browser).googleSearch()
        #except Exception:
            #browser.save_screenshot('.//output//screenshot.png')
            #print(Exception)

@pytest.mark.slow
def test_publish_article_3(browser):
        #try:
            menuPageObj(browser).searchinGoogle("https://www.amazon.in/")
            menuPageObj(browser).googleSearch()
        #except Exception:
            #browser.save_screenshot('.//output//screenshot.png')
            #print(Exception)
