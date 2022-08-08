
from pyallied.web.webElement import common
from pyallied.web.DropDown import DropDownActions
from pyallied.web.browser import Browser

class homePageObj:
     
     obj1="//span[text()='Account & Lists']"
     obj2="//a"
     obj3="//*[@id='searchDropdownBox']"
     obj4="//a[contains(text(),'Best Sellers')]"

     def __init__(self, browser):
         self.browser=browser
         self.me =common(self.browser) 
         self.tik=Browser(self.browser)
         self.user =DropDownActions(self.browser) 
     def searchinGoogle(self,url):
        print(url,'<------->')
        self.me.navigateto(url)
        #assert 0
        #self.browser.get(url)    
     def googleSearch(self):
      try:
        #element= self.me.getAttribute(homePageObj.obj4,"href")
        element= self.user.getFirstSelecteOption(homePageObj.obj3)
        print(element,'<------->')
        self.user.selectDropDownByVisibleText(homePageObj.obj3,"Amazon Fresh")
        
        assert False,"hello"
      except Exception as error:
         self.tik.get_screenshot_png("iamtest")
         raise error
        #assert 0             
        

