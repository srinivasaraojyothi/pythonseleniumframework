from pages.new_drag import DragDrop
from pages.browser_test import Setup


def test_dragdrop(browser):
    DragDrop(browser).launchurl("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
    Setup(browser).Refresh_page()
    DragDrop(browser).DragAndDrop()
