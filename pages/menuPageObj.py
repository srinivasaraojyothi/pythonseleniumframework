from  pyallied.web.webElement import common
#from pyallied.actions.testP import testPrivate

class menuPageObj:
     obj1="//span[text()='Account & Lists']"
     obj2="//a"
     obj3="//*[@id='twotabsearchtextbox']"

     def __init__(self, browser):
         self.browser=browser
         self.me =common(self.browser) 
     def searchinGoogle(self,url):
        self.me.navigateto(url)
        #self.browser.get(url)    
     def googleSearch(self):
        #self.me =testPrivate(self.browser) 
        #Elements= self.me.findElementsBy(menuPageObj.obj2)
        self.me.fillField(menuPageObj.obj3,"mobile")
        assert False,"name"