from numpy import broadcast
from pages.mobile_test import Mobile_Test
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from pages.browser_test import Setup
from pages.new_drag import DragDrop
from pages.windowframes import WindowFrames
from pages.dropdown import DropDown
from pages.web_all_features import Web_Features



def test_features(browser):
    # Setup(browser).FullScreen_window()
    Web_Features(browser).launchurl("https://www.opencart.com/index.php?route=common/home")
    Web_Features(browser).click_login()
    Web_Features(browser).enter_email("sreenivashs3848@gmail.com")
    Web_Features(browser).enter_password("Sree@123")
    Web_Features(browser).submit_login()


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

def test_dragdrop(browser):
    DragDrop(browser).launchurl("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
    DragDrop(browser).DragAndDrop()
    DragDrop(browser).DragAndDropbyOffset()


def test_browser(browser):

    Setup(browser).get_Desired_capabilities_Of_driver()
    Setup(browser).launchurl("https://www.amazon.in/")
    Setup(browser).FullScreen_window()
    Setup(browser).click_on_mobiles()
    Setup(browser).go_Back()
    Setup(browser).Execute_script()
    Setup(browser).launchurl("https://www.twitter.com/")
    Setup(browser).Forward_step()
    Setup(browser).Get_log()
    Setup(browser).Get_pinned_Scripts()
    Setup(browser).Get_page_Load_timeout()
    Setup(browser).Get_implicit_Wait_timeout()
    Setup(browser).Get_Script_timeout()
    Setup(browser).Get_title()
    Setup(browser).Get_application_Cache()
    Setup(browser).Get_current_Url()
    Setup(browser).Get_current_Window_handle()
    Setup(browser).Get_desired_Capabilities()
    Setup(browser).Get_page_Source()
    Setup(browser).get_Command_line_args()
    Setup(browser).get_assert_Process_still_running()
    Setup(browser).get_is_Connectable()
    Setup(browser).get_service_Url()
    Setup(browser).delete_A_Cookie()
    Setup(browser).delete_All_Cookies()
    Setup(browser).Refresh_page()
    # Setup(browser).Execute_command()
    Setup(browser).Set_Page_load_timeout()
    Setup(browser).set_Script_timeout()
    Setup(browser).Set_Window_position()
    Setup(browser).Set_Window_rect()
    Setup(browser).Set_Window_size()
    Setup(browser).Get_cookie()
    Setup(browser).get_Screenshot_ofcurrentActive_page_in_base64()
    Setup(browser).get_Screenshot_ofcurrentActive_page_asFile()
    Setup(browser).get_Screenshot_ofcurrentActive_page_asPNG()
    # Setup(browser).Execut_async_Script()
#     # Setup(browser).close_Driver()

def test_window_switch(browser):
    WindowFrames(browser).launch_url("https://login.yahoo.com/")
    WindowFrames(browser).get_window()
    WindowFrames(browser).get_window_positioN()
    WindowFrames(browser).Get_window_SizE()
    WindowFrames(browser).Minimize_Window()
    WindowFrames(browser).click_elem()
    WindowFrames(browser).SwitchtoWindowUsingHandle()

def test_window_frames(browser):
    WindowFrames(browser).launch_url("https://www.hyrtutorials.com/p/frames-practice.html")
    WindowFrames(browser).SwitchToFrame()
    # WindowFrames(browser).Switch_To_Frame_ByXpatH()
    # WindowFrames(browser).Switch_To_Frame_byIndex()
    # WindowFrames(browser).Switch_To_Frame_byName()