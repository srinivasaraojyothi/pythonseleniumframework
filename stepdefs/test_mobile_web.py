from pages.mobile_test import Mobile_Test
import pytest

class TestMobileWeb:
    me = Mobile_Test

    @pytest.mark.mobilesmoke()
    def test_Mobile_Web(self, browser):
        self.me(browser).goto_Url("https://www.demoblaze.com/")
        self.me(browser).Get_current_url()
        self.me(browser).Get_title()
        self.me(browser).click_sign_up()
        self.me(browser).enter_text()
        self.me(browser).open_window()
        self.me(browser).Switch_toWindoW(1)
        self.me(browser).navigate_url("https://www.2checkout.com/")
        self.me(browser).Get_title()
        self.me(browser).Navigate_back()
        self.me(browser).Refresh_current_page()
        # self.me(browser).Navigate_forward()
        self.me(browser).Get_current_window_handle()
        self.me(browser).Switch_toWindoW(0)
        self.me(browser).Get_title()
        self.me(browser).Switch_toWindoW(1)
        self.me(browser).Get_all_window_handles()
        self.me(browser).Get_window_position()
        self.me(browser).Get_windowSize_Dimensions()
        self.me(browser).Get_window_position()
        self.me(browser).Get_current_url()
        self.me(browser).Get_cookies()
        self.me(browser).Switchto_Frame()
        self.me(browser).enter_email_frame()
        self.me(browser).Switch_to_parent_frame()
        self.me(browser).Switch_to_frame_name()
        self.me(browser).enter_email_frame()
        self.me(browser).Driver_execute_async_script()
