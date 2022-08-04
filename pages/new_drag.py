import time


from pyallied.web.dragAndDrop import DragAndDrop
from pyallied.web.webElement import common
from pyallied.web.webElement_v2 import common_v2
from pyallied.mobile.mobAppium import mobAppium
from pyallied.web.windowAndFrame import frameAndWindow


class DragDrop:
    source_path = "(//div[text()='Rome'])[2]"
    s_p = "(//div[text()='Seoul'])[2]"
    s1 = "//*[@id='box5']"
    destination_path = "//*[@id='box106']"
    s2 = "(//div[text()='Seoul'])[2]"
    d2 = "//div[text()='South Korea']"

    drag_f1 = "//iframe[@class='demo-frame']"
    drag_s1 = "//div[@id='draggable']"
    drag_d1 = "//div[@id='droppable']"

    def __init__(self, browser):
        self.browser = browser
        self.me = common(self.browser)
        self.user = DragAndDrop(self.browser)
        self.web2 = common_v2(self.browser)
        self.mob = mobAppium(self.browser)
        self.fr = frameAndWindow(self.browser)

    def launchurl(self, url):
        self.me.navigateto(url)
    
    def DragAndDropbyOffset1(self):
        self.user.dragAndDropByOffset(DragDrop.s2, 304, -57)
        time.sleep(2)

    def DragAndDrop(self):
        self.user.dragAndDrop(DragDrop.source_path, DragDrop.destination_path)
        time.sleep(2)

    def DragAndDropbyOffset2(self):
        self.fr.switchToFrame(DragDrop.drag_f1)
        self.user.dragAndDropByOffset(DragDrop.drag_s1, 148, 10)
        time.sleep(2)

    def DragAndDrop1(self):
        self.fr.switchToFrame(DragDrop.drag_f1)
        self.user.dragAndDrop(DragDrop.drag_s1, DragDrop.drag_d1)
        time.sleep(2)