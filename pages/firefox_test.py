from time import sleep
from pyallied.web.firefox import firefox
from pyallied.web.webElement import common


class Firefox_Test:
    def __init__(self, browser):
        self.browser = browser
        self.me = firefox(self.browser)
        self.user = common(self.browser)
    
    def launchurl(self, url):
        self.user.navigateto(url)

    def Uninstall_Addon(self):
        self.me.Uninstall_addon("Youtube Audio")
        sleep(5)

    def Install_Addon(self):
        self.me.Install_addon(r"D:\Users\ssreeenivasreddy\Downloads\youtube_audio-0.0.2.5.xpi")

    def Set_Context(self):
        self.me.Set_context("firefox")

    def Get_Firefox_Profile(self):
        a = self.me.Get_firefox_profile("firefox")
        print(a)

    def Add_Extension(self):
        self.me.Add_extension(extension='webdriver.xpi')

    # def Set_Preference(self):
    #     self.me.Set_preference()

    def get_default_Capabilities(self):
        a = self.me.get_default_capabilities()
        print(a)

    # def Update_Capabilities(self):
    #     self.me.Update_capabilities()

    def get_binary_Instance(self):
        a = self.me.get_binary_instance()
        print(a)


    # def Set_accept_untrusted_Certs(self):
    #     self.me.Set_accept_untrusted_certs()

    # def Set_assume_untrusted_cert_Issuer(self):
    #     self.me.Set_assume_untrusted_cert_issuer()

    def get_Encoded_Profile(self):
        a = self.me.Get_encoded_Profile()
        print(a)

    # def Get_Profile_Path(self):
    #     self.me.Get_Profile_path()

    # def Get_Profile_DEFAULT_pREFERENCES(self):
    #     self.me.Get_Profile_DEFAULT_PREFERENCES()

    # def Uninstall_Get_Profile_ANONYMOUS_PROFILE_nAMEAddon(self):
    #     self.me.Get_Profile_ANONYMOUS_PROFILE_NAME()

    # def Get_Profile_Port(self):
    #     self.me.Get_Profile_port()

    # def Add_command_line_Options(self):
    #     self.me.Add_command_line_options()

    # def kill_Binary_Instance(self):
    #     self.me.kill_Binary_instance()

    def Launch_Browser(self):
        self.me.Launch_browser()

    def get_screenshot_OfcurrentActive_page_in_base64(self):
        self.me.get_fullpage_screenshot_as_base64("foo.png")

    def get_screenshot_OfcurrentActive_page_asFile(self):
        self.me.get_fullpage_screenshot_as_File('soo.png')

    def get_screenshot_ofcurrentActive_page_AsPNG(self):
        self.me.get_fullpage_screenshot_as_PNG("dd")

    def screenshot_save_full_paGe_screenshot(self):
        self.me.screenshot_save_full_page_screenshot('fooot.png')