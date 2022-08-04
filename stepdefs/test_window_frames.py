from pages.windowframes import WindowFrames
import pytest
import unittest

class TestFrames:
    me = WindowFrames
    
    @pytest.mark.smoke()
    def test_window_frames(self, browser):
        self.me(browser).launch_url("https://login.yahoo.com/")
        self.me(browser).get_window()
        self.me(browser).get_window_positioN()
        self.me(browser).Get_window_SizE()
        self.me(browser).Minimize_Window()
        self.me(browser).click_elem()
        self.me(browser).SwitchtoWindowUsingHandle()

    @pytest.mark.smoke()
    def test_s(self, browser):
        self.me(browser).launch_url("https://www.hyrtutorials.com/p/frames-practice.html")
        self.me(browser).SwitchToFrame()
