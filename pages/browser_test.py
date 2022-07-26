import time

from pyallied.web.browser import Browser
from pyallied.web.webElement import common
from pyallied.web.webWaits import customwebDriverwait
from pyallied.web.windowAndFrame import frameAndWindow


class Setup:
    a2 = "//a[text()='Mobiles']"
    script = "alert('Alert via sreenivas')"
    script1 = "alert('Alert via sreenivas reddy')"

    def __init__(self, browser):
        self.browser = browser
        self.me = Browser(self.browser)
        self.user = common(self.browser)
        self.u = customwebDriverwait(self.browser)
        self.win = frameAndWindow(self.browser)

    def get_Desired_capabilities_Of_driver(self):
        e = self.me.get_desired_capabilities_Of_driver()
        print(e)

    def launchurl(self, url):
        self.user.navigateto(url)

    def click_on_mobiles(self):
        self.user.click(Setup.a2)

    def go_Back(self):
        self.me.go_back()

    def delete_All_Cookies(self):
        self.me.delete_all_Cookies()

    def delete_A_Cookie(self):
        self.me.delete_a_Cookie('n')

    def Execut_async_Script(self):
        self.me.Execute_Async_Script(Setup.script)

    def Execute_script(self):
        self.me.Execute_Script("window.open()")
        self.win.switchtoWindowUsingHandle(1)

    def Execute_command(self):
        self.me.Execute_Command("n")

    def get_Screenshot_ofcurrentActive_page_in_base64(self):
        self.me.get_screenshot_base64("t1.png")

    def get_Screenshot_ofcurrentActive_page_asFile(self):
        self.me.get_screenshot_file("t2.png")

    def get_Screenshot_ofcurrentActive_page_asPNG(self):
        self.me.get_screenshot_png("t3.png")

    def Forward_step(self):
        self.me.Forward()

    def FullScreen_window(self):
        self.me.FullScreen_Window()

    def Get_cookie(self):
        a = self.me.Get_Cookie("abc")
        print(a)

    def Get_credentials(self):
        a = self.me.Get_Credentials()
        print(a)

    def Get_log(self):
        a = self.me.Get_Log("browser")
        print(a)

    def Get_pinned_Scripts(self):
        a = self.me.Get_pinned_Scripts()
        print(a)

    def Get_page_Load_timeout(self):
        a = self.me.Get_page_load_timeout()
        print(a)

    def Get_implicit_Wait_timeout(self):
        a = self.me.Get_implicit_wait_timeout()
        print(a)

    def Get_Script_timeout(self):
        a = self.me.Get_script_timeout()
        print(a)

    def Get_Virtual_Authenticator_id(self):
        a = self.me.Get_Virtual_authenticator_id()
        print(a)

    def Get_title(self):
        a = self.me.Get_Title()
        print(a)

    def Set_Implicitly_wait(self):
        self.me.Set_implicitly_wait(100)

    # def Pin_Script(self):
    #     self.me.Pin_script()

    def Print_page(self):
        self.me.Print_Page()

    def Refresh_page(self):
        self.me.Refresh()
        time.sleep(5)

    def Remove_all_Credentials(self):
        self.me.Remove_all_credentials()

    def Remove_Credential(self):
        self.me.Remove_credential("123")

    def Remove_Virtual_authenticator(self):
        self.me.Remove_virtual_authenticator()

    def Set_Page_load_timeout(self):
        self.me.Set_page_load_timeout("100")

    def set_Script_timeout(self):
        self.me.set_script_timeout("100")

    # def Set_User_Verified(self):
    #     self.me.Set_user_Verified(verified=Setup.script)

    def Set_Window_position(self):
        self.me.Set_window_position(1024, 1024)

    def Set_Window_rect(self):
        self.me.Set_window_rect(x=10, y=10, width=100, height=200)

    def Set_Window_size(self):
        self.me.Set_window_size(1920, 1080)

    def Start_Client(self):
        self.me.Start_client()

    # def Start_Session(self):
    #     self.me.Start_session(12)

    def Stop_Client(self):
        self.me.Stop_client()

    # def Un_pin(self):
    #     self.me.Unpin()

    def Get_application_Cache(self):
        a = self.me.Get_application_cache()
        print(a)

    def Get_current_Url(self):
        a = self.me.Get_current_url()
        print(a)

    def Get_current_Window_handle(self):
        a = self.me.Get_current_window_handle()
        print(a)

    def Get_desired_Capabilities(self):
        a = self.me.Get_desired_capabilities()
        print(a)

    # def Set_file_Detector(self):
    #     self.me.Set_file_detector()

    def Get_page_Source(self):
        a = self.me.Get_Page_Source()
        print(a)

    def get_Command_line_args(self):
        a = self.me.get_command_line_args()
        print(a)

    def get_assert_Process_still_running(self):
        a = self.me.get_assert_process_still_running()
        print(a)

    def get_is_Connectable(self):
        a = self.me.get_is_connectable()
        print(a)

    def Send_remote_shutdown_Command(self):
        self.me.Send_remote_shutdown_command()

    def start_Service(self):
        self.me.start_service()

    def stop_Service(self):
        self.me.stop_service()

    def get_service_Url(self):
        a = self.me.get_service_url()
        print(a)

    def close_Driver(self):
        self.me.close_driver()
