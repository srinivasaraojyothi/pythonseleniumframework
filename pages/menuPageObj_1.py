from  pyallied.web.webElement import common
from pyallied.web.browser import Browser
from pages.base import Base
#from pyallied.actions.testP import testPrivate

class menuPageObj(Base):
     obj1="//span[text()='Account & Lists']"
     obj2="//a"
     obj3="//*[@id='twotabsearchtextbox']"

     def __init__(self, browser):
         super().__init__(self,browser)
     def searchinGoogle(self,url):
        super().me.navigateto(url)
        #self.browser.get(url)    
     def googleSearch(self):
      try:
        #self.me =testPrivate(self.browser) 
        #Elements= self.me.findElementsBy(menuPageObj.obj2)
        super().me.fillField(menuPageObj.obj3,"mobile")
        assert False,"name"
      except Exception as error:
         super().tik.get_screenshot_png("iamtest")
         raise error        