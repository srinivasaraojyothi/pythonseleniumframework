from pages.dropdown import DropDown


def test_dropDown(browser):
    DropDown(browser).launchurl("https://selenium08.blogspot.com/2019/11/dropdown.html")
    DropDown(browser).SelectDropDownByVisibleText()
    DropDown(browser).SelectDropDownByIndex()
    DropDown(browser).selectDropDownByvalue()
    DropDown(browser).getDefaultSelectedDropDownoptions()
    DropDown(browser).getAllOptionIndropDown()
    DropDown(browser).getfirstSelecteOption()
    DropDown(browser).deselectAllOptionsIndropDown()
    DropDown(browser).SelectDropDownByVisibleText()
    DropDown(browser).SelectDropDownByIndex()
    DropDown(browser).selectDropDownByvalue()
    DropDown(browser).DeselectByIndex()
    DropDown(browser).deselectByvalue()
    DropDown(browser).deselectByVisibletext()

