from pathlib2 import Path
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenarios, given, when, then
from pages.homePageObj import homePageObj


scenarios("homefeatures")
@given("I press the publish button")
def article(browser):
    homePageObj(browser).searchinGoogle("https://www.amazon.in/")
   # print(' in step----------')
@then("do the google search")
def article2(browser):   
    homePageObj(browser).googleSearch()
@then("do the amazon search")
def article3(browser):   
    homePageObj(browser).googleSearch()    
@then("go to the google search")
def article4(browser):   
    homePageObj(browser).searchinGoogle("https://www.google.com/")       