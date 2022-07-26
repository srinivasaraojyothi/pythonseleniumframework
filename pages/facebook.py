from pyallied.web.webElement import common
from pyallied.web.DropDown import DropDownActions


class CreateAccount:
    obj1 = "//a[text()='Create New Account']"
    obj2 = "//input[@name='firstname']"
    obj3 = "//input[@name='lastname']"
    obj4 = "//input[@name='reg_email__']"
    obj5 = "//input[@name='reg_passwd__']"
    obj6 = "//select[@id='day']"
    obj7 = "//select[@id='month']"
    obj8 = "//select[@id='year']"
    obj9 = "//label[text()='Male']"
    obj10 = "//button[@name='websubmit']"

    def __init__(self, browser):
        self.browser = browser
        self.me = common(self.browser)
        self.user = DropDownActions(self.browser)

    def search_url(self, url):
        self.me.navigateto(url)

    def click_create_new_account(self):
        if self.me.isElementDisplayed(CreateAccount.obj1):
            self.me.click(CreateAccount.obj1)
        else:
            print("element is not displayed")

    def enter_first_name(self, text):
        self.me.fillField(CreateAccount.obj2, text)
        self.me.clear(CreateAccount.obj2)
        self.me.fillField(CreateAccount.obj2, text)

    def enter_surname(self, text):
        self.me.fillField(CreateAccount.obj3, text)

    def enter_email(self, text):
        self.me.fillField(CreateAccount.obj4, text)

    def enter_password(self, text):
        self.me.fillField(CreateAccount.obj5, text)

    def select_day(self):
        self.user.getFirstSelecteOption(CreateAccount.obj6)
        self.user.selectDropDownByVisibleText(CreateAccount.obj6, "5")

    def select_month(self):
        self.user.selectDropDownByValue(CreateAccount.obj7, "8")

    def select_year(self):
        self.user.getFirstSelecteOption(CreateAccount.obj8)
        self.user.selectDropDownByVisibleText(CreateAccount.obj8, "1995")

    def select_gender(self):
        if self.me.isElementEnabled(CreateAccount.obj9):
            self.me.click(CreateAccount.obj9)
            if self.me.isElementSelected(CreateAccount.obj9):
                print("element is selected")
        else:
            print("element is not enabled")

    def click_signup(self):
        self.me.moveToElement(CreateAccount.obj10)
        self.me.actionClick(CreateAccount.obj10)





