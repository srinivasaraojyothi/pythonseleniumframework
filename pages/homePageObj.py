
from pyseleniumbot.web.webElement import common
from pyseleniumbot.web.DropDown import DropDownActions
class homePageObj:
     
     obj1="//span[text()='Account & Lists']"
     obj2="//a"
     obj3="//*[@id='searchDropdownBox']"
     obj4="//a[contains(text(),'Best Sellers')]"

     def __init__(self, browser):
         self.browser=browser
         self.me =common(self.browser) 
         self.user =DropDownActions(self.browser) 
     def searchinGoogle(self,url):
        print(url,'<------->')
        self.me.navigateto(url)
        #assert 0
        #self.browser.get(url)    
     def googleSearch(self):

        #element= self.me.getAttribute(homePageObj.obj4,"href")
        element= self.user.getFirstSelecteOption(homePageObj.obj3)
        print(element,'<------->')
        self.user.selectDropDownByVisibleText(homePageObj.obj3,"Amazon Fresh")
        #assert False,"hello"

        #assert 0            
                

