from pages.dropdown import DropDown
import pytest
import unittest

class TestDropDown:
    me = DropDown

    @pytest.mark.smoke()
    def test_dropDown(self, browser):
        self.me(browser).launchurl("https://selenium08.blogspot.com/2019/11/dropdown.html")
        self.me(browser).SelectDropDownByVisibleText()
        self.me(browser).SelectDropDownByIndex()
        self.me(browser).selectDropDownByvalue()
        self.me(browser).getDefaultSelectedDropDownoptions()
        self.me(browser).getAllOptionIndropDown()
        self.me(browser).getfirstSelecteOption()
        self.me(browser).deselectAllOptionsIndropDown()
        self.me(browser).SelectDropDownByVisibleText()
        self.me(browser).SelectDropDownByIndex()
        self.me(browser).selectDropDownByvalue()
        self.me(browser).DeselectByIndex()
        self.me(browser).deselectByvalue()
        self.me(browser).deselectByVisibletext()

