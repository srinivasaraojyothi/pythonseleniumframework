
from pyallied.web.webElement import common
from pyallied.web.DropDown import DropDownActions
from pyallied.web.browser import Browser
class Base:
     def __init__(self, browser):
         self.browser=browser
         self.me =common(self.browser) 
         self.tik=Browser(self.browser)
         self.user =DropDownActions(self.browser) 
        