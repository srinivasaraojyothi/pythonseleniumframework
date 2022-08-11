import logging
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
class MyListener(AbstractEventListener):
    def after_change_value_of(self,element, driver):
        print("after_change_value_of %s" % element)
    def after_click(self,element, driver):
        print("Aafter_click %s" % element)
    def after_close(self,driver):
        print("after_close %s" % driver)
    def after_execute_script(self,script, driver):
        print("after_execute_script %s" % script)
    def after_find(self,by, value, driver):
        print("after_find %s" % by," = ",self.__init_subclass__," <<>>",value)
    def after_navigate_back(self,driver):
        print("after_navigate_back %s" % driver)
    def after_navigate_forward(self,driver):
        print("after_navigate_forward %s" % driver)
    def after_navigate_to(self,url, driver):
        print("after_navigate_to %s" % url)
    def after_quit(self,driver):
        print("after_quit %s" % driver)
    def before_change_value_of(self,element, driver):
        print("before_change_value_of %s" % element)
    def before_click(self,element, driver):
        print("before_click %s" % element)
    def before_close(self,driver):
        print("before_close %s" % driver)
    def before_execute_script(self,script, driver):
        print("before_execute_script %s" % script)
    def before_find(self,by, value, driver):
        print("before_find %s" % by," = ",value,driver)
    def before_navigate_back(self,driver):
        print("before_navigate_back %s" % driver)
    def before_navigate_forward(self,driver):
        print("before_navigate_forward %s" % driver)
    def before_navigate_to(self,url, driver):
        print("before_navigate_to %s" % url)
    def before_quit(self,driver):
        print("before_quit %s" % driver)
    def on_exception(self,exception, driver):
        print("on_exception %s" % exception) 
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebElement
class Mylistner_2():
    def click():
        print("click----")        
                      