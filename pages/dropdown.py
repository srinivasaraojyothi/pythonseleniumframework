import time

from pyallied.web.DropDown import DropDownActions

from pyallied.web.webElement import common
from pyallied.web.browser import Browser


class DropDown:
    a1 = "//select[@name='Month']"

    def __init__(self, browser):
        self.browser = browser
        self.me = common(self.browser)
        self.user = DropDownActions(self.browser)

    def launchurl(self, url):
        self.me.navigateto(url)

    def SelectDropDownByVisibleText(self):
        self.user.selectDropDownByVisibleText(DropDown.a1, "May")
        time.sleep(2)

    # def selectDropDownByValue(self):
    #     self.user.selectDropDownByValue()

    def SelectDropDownByIndex(self):
        self.user.selectDropDownByIndex(DropDown.a1, "3")
        time.sleep(2)

    def selectDropDownByvalue(self):
        self.user.selectDropDownByValue(DropDown.a1, "Ap")
        time.sleep(2)

    def getDefaultSelectedDropDownoptions(self):
        a = self.user.getDefaultSelectedDropDownOptions(DropDown.a1)
        print(a)

    def getAllOptionIndropDown(self):
        b = self.user.getAllOptionInDropDown(DropDown.a1)
        print(b)

    def getfirstSelecteOption(self):
        a = self.user.getFirstSelecteOption(DropDown.a1)
        print(a)

    def deselectAllOptionsIndropDown(self):
        self.user.deselectAllOptionsInDropDown(DropDown.a1)
        time.sleep(2)

    def DeselectByIndex(self):
        self.user.deselectByIndex(DropDown.a1, "3")
        time.sleep(2)

    def deselectByvalue(self):
        self.user.deselectByValue(DropDown.a1, "Ap")
        time.sleep(2)

    def deselectByVisibletext(self):
        self.user.deselectByVisibleText(DropDown.a1, "May")
        time.sleep(2)

