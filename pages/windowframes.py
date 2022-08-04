from time import sleep
from pyallied.web.windowAndFrame import frameAndWindow
from pyallied.web.webElement import common
from pyallied.web.browser import Browser
from pyallied.web.DropDown import DropDownActions


class WindowFrames:

    a1 = "//a[text()='Privacy']"
    a2 = "(//input[@id='name'])[1]"
    frame1 = "(//iframe[@id='frm1'])[1]"
    frame2 = "(//iframe[@id='frm2'])[1]"
    f1 = "(//select[@class='selectnav'])[1]"

    def __init__(self, browser):
        self.browser = browser
        self.me = common(self.browser)
        self.user = frameAndWindow(self.browser)
        self.you = Browser(self.browser)
        self.i = DropDownActions(self.browser)

    def launch_url(self, url):
        self.me.navigateto(url)

    def get_window(self):
        a= self.user.Get_Window_handles()
        print(a)

    def get_window_positioN(self):
        a = self.user.Get_window_Position()
        print(a)
    
    def Get_window_SizE(self):
        a = self.user.Get_window_size()
        print(a)

    def Minimize_Window(self):
        self.user.Minimize_window()

    def click_elem(self):
        self.me.click(WindowFrames.a1)
        sleep(2)
    
    # def switchtoWindowusingName(self):
    #     self.user.switchToWindowUsingName()
    #
    def SwitchtoWindowUsingHandle(self):
        self.user.switchtoWindowUsingHandle(1)
        print("Second window title =" + self.you.Get_Title() )
        self.user.switchtoWindowUsingHandle(0)
        print("First window title =" + self.you.Get_Title() )


    def SwitchToFrame(self):
        self.me.fillField(WindowFrames.a2, "sreenivas")
        self.user.switchToFrame(WindowFrames.frame1)
        self.i.selectDropDownByVisibleText(WindowFrames.f1, "Home")
        sleep(2)
        self.user.switchToParentFrame()
        self.me.clear(WindowFrames.a2)
        self.me.fillField(WindowFrames.a2, "sreenivas reddy")

    def Switch_To_Frame_ByXpatH(self):
        self.user.switch_To_Frame_ByXpath(WindowFrames.frame2)
        self.i.selectDropDownByVisibleText(WindowFrames.f1, "Telugu")
    
    #
    def Switch_To_Frame_byIndex(self):
        self.me.click(WindowFrames.a2)
        self.me.click(WindowFrames.a3)
        self.user.switch_To_Frame_ByIndex(0)
    #
    def Switch_To_Frame_byName(self):
        self.user.switchToFrame(WindowFrames.a2)
        self.me.click(WindowFrames.a2)
        self.me.click(WindowFrames.a3)
        self.user.switch_To_Frame_ByName("frame-top")
    #
    # def Switch_To_Parent_Frame(self):
    #     self.user.switchToParentFrame()

