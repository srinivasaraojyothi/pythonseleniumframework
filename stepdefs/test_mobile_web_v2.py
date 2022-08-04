from pages.mobile_test import Mobile_Web_V2
import pytest
import unittest

class TestMobileWebElemnts:
    me = Mobile_Web_V2

    @pytest.mark.smoke()
    def test_Mobile_Web(self, browser):
        self.me(browser).launch_url("https://www.demoblaze.com/")
        self.me(browser).keydown_and_sendKeys()
        self.me(browser).enter_user_name("sreenivashs38@gmail.com")
        self.me(browser).enter_password("sree.123")
        self.me(browser).clear_element()
        self.me(browser).enter_password("sree.123")
        self.me(browser).click_login2()
        self.me(browser).GetAttribute()
        self.me(browser).GetDomAttribute()
        self.me(browser).GetProperty()
        self.me(browser).CurrentElementscreenshot()
        self.me(browser).click_action()
        self.me(browser).click_action_hold()
        self.me(browser).AcceptAlert()
        self.me(browser).move_element()
        self.me(browser).AcceptAlert()
        self.me(browser).move_element_click()
        self.me(browser).AcceptAlert()
        self.me(browser).open_new_window()
        self.me(browser).Switch_toWindoW(1)
        self.me(browser).launch_url("https://www.mohfw.gov.in/")
        # Mobile_Web_V2(browser).move_element_click_sub()
        self.me(browser).Switch_toWindoW(0)
        self.me(browser).MoveToElementWithOffset()
        self.me(browser).ResetActions()
        self.me(browser).open_new_window()
        self.me(browser).Switch_toWindoW(2)
        self.me(browser).launch_url("https://www.cowin.gov.in/")
        self.me(browser).Get_Value_of_css_property()
        # Mobile_Web_V2(browser).Get_Accessible_name()
        # Mobile_Web_V2(browser).Get_Aria_role()
        # Mobile_Web_V2(browser).Get_Element_shadow_root()
        self.me(browser).get_internal_ID()
        self.me(browser).get_location_of_Element()
        self.me(browser).Get_Scroll_location_of_Element()
        self.me(browser).Get_Prent_of_Element()
        self.me(browser).Get_size_And_Location()
        self.me(browser).Get_Element_size()
        self.me(browser).Get_Element_text()
        
    @pytest.mark.smoke()
    def test_right_double_click(self,browser):
        self.me(browser).launch_url("https://demoqa.com/buttons")
        self.me(browser).Right_Click()
        self.me(browser).Double_click()

    @pytest.mark.smoke()
    def test_drag_drop(self,browser):
        self.me(browser).launch_url("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
        self.me(browser).DragAndDrop()
        self.me(browser).DragAndDropByOffset()

    @pytest.mark.smoke()
    def test_drop_down(self, browser):
        self.me(browser).launch_url("https://selenium08.blogspot.com/2019/11/dropdown.html")
        self.me(browser).SelectDropDownByVisibleText()
        self.me(browser).SelectDropDownByIndex()
        self.me(browser).SelectDropDownByValue()
        self.me(browser).GetDefaultSelectedDropDownOptions()
        self.me(browser).GetAllOptionInDropDown()
        self.me(browser).GetFirstSelecteOption()
        self.me(browser).DeselectAllOptionsInDropDown()
        self.me(browser).SelectDropDownByVisibleText()
        self.me(browser).SelectDropDownByIndex()
        self.me(browser).SelectDropDownByValue()
        self.me(browser).DeselectByIndex()
        self.me(browser).DeselectByVisibleText()
        self.me(browser).DeselectByValue()