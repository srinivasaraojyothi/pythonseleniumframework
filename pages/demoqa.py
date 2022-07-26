import time

from pyallied.web.webElement import common
from pyallied.web.DropDown import DropDownActions
from selenium.webdriver import Keys


class PracticeForm:
    body = "/html/body"
    # form = "//h5[text()='Forms']"
    form = "(//div[@class='card-up'])[3]"
    form1 = "(//span[@class='pr-1'])[2]"
    practice_form = "//span[text()='Practice Form']"
    fn = "//input[@id='firstName']"
    ln = "//input[@id='lastName']"
    email = "(//input[@id='userEmail'])"
    gm = "//label[text()='Male']"
    gf = "//label[text()='Female']"
    go = "//label[text()='Other']"
    mn = "//input[@id='userNumber']"
    dob = "//input[@id='dateOfBirthInput']"
    dob_m = "//select[@class='react-datepicker__month-select']"
    dob_y = "//select[@class='react-datepicker__year-select']"
    dob_d = "(//div[@class='react-datepicker__day react-datepicker__day--005 react-datepicker__day--weekend'])"
    sub = "//input[@id='subjectsInput']"
    upload_pic = "//input[@id='uploadPicture']"
    address = "//textarea[@id='currentAddress']"
    image = "//img[@src='/images/Toolsqa.jpg']"

    ele = "(//span[@class='pr-1'])[1]"
    dc = "//button[@id='doubleClickBtn']"
    verify_dc = "//p[@id='doubleClickMessage']"
    rc = "//button[@id='rightClickBtn']"
    verify_rc = "//p[@id='rightClickMessage']"
    chk_box = "//span[text()='Check Box']"
    chk_home = "//span[text()='Home']"
    buttons = "//span[text()='Buttons']"

    def __init__(self, browser):
        self.browser = browser
        self.me = common(self.browser)
        self.user = DropDownActions(self.browser)

    def launch_url(self, url):
        self.me.navigateto(url)

    def image_dis(self):
        if self.me.isElementDisplayed(PracticeForm.image):
            assert True
        else:
            print("not displayed")

    def click_form(self):
        self.me.moveToElement(PracticeForm.form)
        self.me.actionClick(PracticeForm.form)
        # self.me.click(PracticeForm.form)

    def click_practice_form(self):
        if self.me.isElementEnabled(PracticeForm.form1):
            self.me.moveToElement(PracticeForm.form1)
            self.me.actionClick(PracticeForm.form1)
            self.me.actionClick(PracticeForm.practice_form)
        else:
            print("not enabled")

    def enter_fn(self, text):
        self.me.fillField(PracticeForm.fn, text)

    def enter_ln(self, text):
        self.me.fillField(PracticeForm.ln, text)

    def enter_email(self, text):
        self.me.fillField(PracticeForm.email, text)
        self.me.clear(PracticeForm.email)
        time.sleep(2)

    def select_gender(self):
        self.me.click(PracticeForm.gm)

    def enter_phone(self, text):
        self.me.fillField(PracticeForm.mn, text)

    def select_dob(self):
        if self.me.isElementEnabled(PracticeForm.dob):
            self.me.click(PracticeForm.dob)
            self.user.getFirstSelecteOption(PracticeForm.dob_m)
            self.user.selectDropDownByVisibleText(PracticeForm.dob_m, "August")
            self.user.getFirstSelecteOption(PracticeForm.dob_y)
            self.user.selectDropDownByVisibleText(PracticeForm.dob_y, "1995")
            time.sleep(2)
            self.me.click(PracticeForm.dob_d)
        else:
            print("element is not enabled")

    def enter_subject(self, text):
        self.me.fillField(PracticeForm.sub, text)
        time.sleep(2)


class Element:
    ele = "(//span[@class='pr-1'])[1]"
    dc = "//button[@id='doubleClickBtn']"
    verify_dc = "//p[@id='doubleClickMessage']"
    rc = "//button[@id='rightClickBtn']"
    verify_rc = "//p[@id='rightClickMessage']"
    chk_box = "//span[text()='Check Box']"
    chk_home = "//span[text()='Home']"
    buttons = "//span[text()='Buttons']"
    elem = "(//div[@class='card-up'])[1]"

    def __init__(self, browser):
        self.browser = browser
        self.me = common(self.browser)
        self.user = DropDownActions(self.browser)

    def launch_url(self, url):
        self.me.navigateto(url)

    def click_element(self):
        self.me.click(Element.elem)

    def click_elements(self):
        self.me.moveToElement(Element.ele)
        self.me.click(Element.ele)

