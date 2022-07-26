import time


from pyallied.web.dragAndDrop import DragAndDrop
from pyallied.web.webElement import common


class DragDrop:
    # source_path = "//div[@id='draggable']"
    # destination_path = "//div[@id='droppable']"
    source_path = "//*[@id='box6']"
    s1 = "//*[@id='box5']"
    destination_path = "//*[@id='box106']"

    def __init__(self, browser):
        self.browser = browser
        self.me = common(self.browser)
        self.user = DragAndDrop(self.browser)

    def launchurl(self, url):
        self.me.navigateto(url)

    def DragAndDrop(self):
        self.user.dragAndDrop(DragDrop.source_path, DragDrop.destination_path)
        time.sleep(2)

    def DragAndDropbyOffset(self):
        time.sleep(2)
        self.user.dragAndDropByOffset(DragDrop.s1, 110, 65)
