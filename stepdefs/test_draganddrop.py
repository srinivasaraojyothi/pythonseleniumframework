from pages.new_drag import DragDrop
import pytest
import unittest

class TestDragDrop:
    me = DragDrop
    
    @pytest.mark.smoke()
    def test_dragdrop_demo(self, browser):
        self.me(browser).launchurl("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
        self.me(browser).DragAndDrop()
        self.me(browser).DragAndDropbyOffset1()

    # def test_dragdrop_demo1(browser):
    #     DragDrop(browser).launchurl("https://jqueryui.com/droppable/")
    #     DragDrop(browser).DragAndDrop1()
    
    @pytest.mark.smoke()
    def test_dragdrop_demo2(self, browser):
        self.me(browser).launchurl("https://jqueryui.com/droppable/")
        self.me(browser).DragAndDropbyOffset2()