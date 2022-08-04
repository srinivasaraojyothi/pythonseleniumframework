from pages.browser_test import Setup
import pytest
import unittest

class TestBrowser:
    me = Setup

    @pytest.mark.smoke()
    def test_brow(self, browser):

        self.me(browser).get_Desired_capabilities_Of_driver()
        self.me(browser).launchurl("https://www.amazon.in/")
        self.me(browser).FullScreen_window()
        self.me(browser).click_on_mobiles()
        self.me(browser).go_Back()
        self.me(browser).Execute_script()
        self.me(browser).launchurl("https://www.twitter.com/")
        self.me(browser).Forward_step()
        self.me(browser).Get_log()
        self.me(browser).Get_pinned_Scripts()
        self.me(browser).Get_page_Load_timeout()
        self.me(browser).Get_implicit_Wait_timeout()
        self.me(browser).Get_Script_timeout()
        self.me(browser).Get_title()
        self.me(browser).Get_application_Cache()
        self.me(browser).Get_current_Url()
        self.me(browser).Get_current_Window_handle()
        self.me(browser).Get_desired_Capabilities()
        self.me(browser).Get_page_Source()
        self.me(browser).get_Command_line_args()
        self.me(browser).get_assert_Process_still_running()
        self.me(browser).get_is_Connectable()
        self.me(browser).get_service_Url()
        self.me(browser).delete_A_Cookie()
        self.me(browser).delete_All_Cookies()
        self.me(browser).Refresh_page()
        self.me(browser).Set_Page_load_timeout()
        self.me(browser).set_Script_timeout()
        self.me(browser).Set_Window_position()
        self.me(browser).Set_Window_rect()
        self.me(browser).Set_Window_size()
        self.me(browser).Get_cookie()
        self.me(browser).get_Screenshot_ofcurrentActive_page_in_base64()
        self.me(browser).get_Screenshot_ofcurrentActive_page_asFile()
        self.me(browser).get_Screenshot_ofcurrentActive_page_asPNG()
        # self.me(browser).Execut_async_Script()








