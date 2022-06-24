
from selenium.webdriver import ActionChains

from selenium.common.exceptions import NoSuchElementException
import polling2, time

from appium.webdriver.extensions.execute_mobile_command import ExecuteMobileCommand
from appium.webdriver.common.appiumby import AppiumBy
from pyseleniumbot.web.webElement import common
from pyseleniumbot.web.DropDown import DropDownActions
from pyseleniumbot.mobile.pollWait import pollWait
from pyseleniumbot.mobile.mobAppium import mobAppium
from pyseleniumbot.mobile.session import session
class airbnbPage:
     
    obj1="//*[@content-desc='Close']"
    obj2="//*[@text='Log in or sign up to Airbnb'']"

    def __init__(self, browser):
         self.browser=browser
         self.me =common(self.browser) 
         self.user =DropDownActions(self.browser)
         self.wait =pollWait(self.browser)
         self.mobAppium =mobAppium(self.browser)
         
    def VerifyUserisOnloginPage(self):
         self.wait.with_findElements_byXpath(airbnbPage.obj1)
         
         #print(self.session.get_Contexts())
         #polling2.poll(lambda: self.browser.find_element(MobileBy.XPATH, airbnbPage.obj1),ignore_exceptions=(NoSuchElementException,), step=5, timeout=30)
         #WebDriverWait(self.browser, 50).until(EC.find_element((AppiumBy.XPATH, airbnbPage.obj1)))
         actions = ActionChains(self.browser)
         #self.browser.implicitly_wait(25)
         menu =self.mobAppium.find_elementBy("XPATH", airbnbPage.obj2)
         print(menu,'<---------->')
         actions.move_to_element(menu)
         actions.click()
         actions.perform()


         #self.me.WaitFor_PresenseOf_Element_Located(airbnbPage.obj2)
         
         #self.me.WaitFor_VisibilityOf_Element_Located(airbnbPage.obj2)
         #menu =self.browser.find_element(By.XPATH, airbnbPage.obj1)
         #ActionChains(self.browser).move_to_element(menu).click(menu)
         #self.me.click(airbnbPage.obj1)
         #self.me.getProperty(airbnbPage.obj2,"text")
         #assert False
