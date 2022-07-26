from pages.windowframes import WindowFrames


# def test_window_frames(browser):
#     WindowFrames(browser).launch_url("https://login.yahoo.com/")
#     # WindowFrames(browser).get_window()
#     # WindowFrames(browser).get_window_positioN()
#     # WindowFrames(browser).Get_window_SizE()
#     # WindowFrames(browser).Minimize_Window()
#     WindowFrames(browser).click_elem()
#     WindowFrames(browser).SwitchtoWindowUsingHandle()

def test_s(browser):
    WindowFrames(browser).launch_url("https://www.hyrtutorials.com/p/frames-practice.html")
    WindowFrames(browser).SwitchToFrame()
    # WindowFrames(browser).Switch_To_Frame_ByXpatH()
    # WindowFrames(browser).Switch_To_Frame_byIndex()
    # WindowFrames(browser).Switch_To_Frame_byName()