
from  pyallied.web.webElement import common
from  pyallied.web.webElement_v2 import common_v2
from pyallied.web.browser import Browser
import time
from pytest_html import extras,plugin
import logging
from logging import config 
log_config_ini = "pytest.ini"
logging.config.fileConfig(log_config_ini)

logger = logging.getLogger()
#from pyallied.actions.testP import testPrivate

class menuPageObj:
     obj1="//span[text()='Account & Lists']"
     obj2="//a"
     obj3="//*[@id='twotabsearchtextbox']"

     def __init__(self, browser):
         self.browser=browser
         #self.extra=extra
         self.me =common(self.browser)
         self.tik=Browser(self.browser) 
         self.v2=common_v2(self.browser)
     def searchinGoogle(self,url):
        self.me.navigateto(url)
        time.sleep(5)
        logger.critical('This outputs just to the scre_critical')
        logger.info("This does not write to either screen (expected) nor file (unexpected)_info") 
        logger.debug("debug")  
        logger.exception("exception----")  
        logger.warning("warning----")  
        #self.browser.get(url)    
     def googleSearch(self):
      try:
        #self.me =testPrivate(self.browser) 
        #Elements= self.me.findElementsBy(menuPageObj.obj2)
        self.me.fillField(menuPageObj.obj3,"mobile")
        assert "srini","srini"
      except Exception as error:
         self.tik.get_screenshot_png("iamtest")
         raise error 
     def edurekha(self):
      try:
        #self.me =testPrivate(self.browser) 
        #Elements= self.me.findElementsBy(menuPageObj.obj2)
        
        print(' i am here-1-')
        test=self.v2.switch_To_Frame_ByAnyLocator("xpath","//*[@class='demo-frame']")
        #print(test,'<---------->')
        time.sleep(5)
        self.v2.dragAndDrop("id","draggable","droppable")
        #self.v2.moveToElement_and_click("xpath","//nav/div[1]/a/span/b")
        #time.sleep(5)
        #self.v2.moveToElement_and_subElement_click("xpath","//nav/div[1]/ul/li[1]/a[text()='Cloud Computing']","//li[1]/ul/li[1]/a[text()='Cloud Architect Masters Program']")
        #assert False,"data"
        #print(' i am here-2-')
      except Exception as error:
         #self.extra.append(extras.image('D:\\Users\\sjyothi\\Repos\\pythonseleniumFramework\\logo\\jci_logo.png'))
         self.tik.get_screenshot_png("iamtest")
         raise error
         
     def searchText(self):
      try:   
        self.v2.click("xpath","//input[@name='q']")
        self.v2.sendKeys("iit chennai")
      except Exception as error:
        raise error                      