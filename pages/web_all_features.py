import time

from pyallied.web.browser import Browser
from pyallied.web.webElement import common
from pyallied.web.webWaits import customwebDriverwait
from pyallied.web.windowAndFrame import frameAndWindow


class Web_Features:

        def __init__(self, browser):
                self.browser = browser
                self.br = Browser(self.browser)
                self.cn = common(self.browser)
                self.cw = customwebDriverwait(self.browser)
                self.win = frameAndWindow(self.browser)

        login = "(//a[@href='https://www.opencart.com/index.php?route=account/login'])[2]"
        email = "//input[@id='input-email']"
        password = "//input[@id='input-password']"
        submit = "(//button[@type='submit'])[1]"


        def launchurl(self, url):
                self.cn.navigateto(url)

        def click_login(self):
                self.cn.click(Web_Features.login)

        def enter_email(self, a):
                self.cn.fillField(Web_Features.email, a)

        def enter_password(self, a):
                self.cn.fillField(Web_Features.password, a)

        def submit_login(self):
                self.cn.click(Web_Features.submit)



        

