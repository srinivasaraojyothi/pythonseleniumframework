from selenium.webdriver import ActionChains

from selenium.common.exceptions import NoSuchElementException
import polling2, time

from appium.webdriver.extensions.execute_mobile_command import ExecuteMobileCommand
from appium.webdriver.common.appiumby import AppiumBy
from pyallied.web.webElement import common
from pyallied.web.DropDown import DropDownActions
from pyallied.mobile.pollWait import pollWait
from pyallied.mobile.mobAppium import mobAppium
from pyallied.mobile.session import session
from pyallied.mobile.mobAppium_actions import mobAppium_actions
from pyallied.web.webElement import common
from pyallied.web.browser import Browser
from pyallied.web.windowAndFrame import frameAndWindow

class Mobile_Test:

    phone = "com.airbnb.android:id/2131428932"
    a1 = "//*[@text='Log In']"
    id = "com.airbnb.android:id/2131429499"
    a2 =  "Close"
    a3 = "//*[@text='Continue with Email']"
    a4 = "//*[@text='Email']"
    clock1 = "//*[@text='ALARM']"
    clear_id = "com.airbnb.android:id/2131428932"
    get_txt_id = "com.airbnb.android:id/2131432821"
    get_text_xp = "//*[@text='Log in or sign up to Airbnb']"
    a5 = "//*[@text='Continue with Phone']"
    a6 = "//android.view.View[@content-desc='Amazing pools']"
    a7 = "//*[@text='Where to?']"
    a8 = "//*[@text='Search destinations']"
    a9 = "com.airbnb.android:id/search_input"
    script = "alert('Alert via sreenivas')"
    css = "//*[@text='Continue with Apple']"
    scripts = """
    const el = await driver.$('~foo');
    await el.click();
    
"""
    touch = "//*[@text='MV, Maldives']"
    touch1 = "//*[@text='Anambas, Indonesia']"

    w1 = "//*[@text='IMAGES']"
    w2 = "//a[@id='signin2']"
    w3 = "//a[text()='Click Here']"
    w4 = "//input[@id='sign-username']"
    w5 = "//input[@id='sign-password']"
    w6 = "(//button[text()='Close'])[2]"
    w7 = "//input[@id='Email']"
    w8 = "(//a[text()='SIGN UP for FREE'])[3]"
    frame1 = "//iframe[@id='newsletter-signup-form']"

    def __init__(self, browser):
         self.browser=browser
         self.me =mobAppium_actions(self.browser) 
         self.user =DropDownActions(self.browser)
         self.wait =pollWait(self.browser)
         self.mobAppium =mobAppium(self.browser)
         self.u = common(self.browser)
         self.br = frameAndWindow(self.browser)
    def Click_element(self):
        # self.me.click("ACCESSIBILITY_ID", Mobile_Test.a2)
        self.me.click("XPATH", Mobile_Test.a3)
        self.me.click("XPATH", Mobile_Test.a4)
    def entertext(self):
        self.me.send_Keys("XPATH", Mobile_Test.a4, "sreenivashs38@gmail.com")

    def Clear_element(self):
        self.me.clear("XPATH", Mobile_Test.a4)
        self.me.send_Keys("XPATH", Mobile_Test.a4, "sreenivashs38@gmail.com")

    def GetText(self):
        a = self.me.get_text("XPATH", Mobile_Test.get_text_xp)
        print(a)

    def get_TagName(self):
        a = self.me.get_tagName("XPATH", Mobile_Test.get_text_xp)
        print(a)

    def Get_Attribute(self):
        a = self.me.get_attribute("XPATH", Mobile_Test.get_text_xp, "package")
        print(a)

    def is_enabled(self):
        if self.me.is_Enabled("XPATH", Mobile_Test.get_text_xp):
            print("Enabled")
    
    def is_displayed(self):
        a = self.me.is_Displayed("XPATH", Mobile_Test.get_text_xp)
        print(a)

    def is_selected(self):
        if self.me.is_Selected("XPATH", Mobile_Test.get_text_xp):
            print("seleted")
        else:
            print("not selected")

    def get_Location(self):
        a = self.me.get_location("XPATH", Mobile_Test.get_text_xp)
        print(a)

    def get_Element_Size_inPixel(self):
        a = self.me.get_Element_size_inPixel("XPATH", Mobile_Test.get_text_xp)
        print(a)

    def get_Element_dimensions_Coordinates(self):
        a = self.me.get_Element_dimensions_coordinates("XPATH", Mobile_Test.get_text_xp)
        print(a)

    def get_value_of_Css_property(self):
        a = self.me.get_value_of_css_property("XPATH", Mobile_Test.css, "color")
        print(a)

    def get_location_in_View(self):
        a = self.me.get_location_in_view("XPATH", Mobile_Test.get_text_xp)
        print(a)

    def submit_form_element(self):
        self.me.submit_Form_element("XPATH", Mobile_Test.a3)

    def get_active_Element(self):
        a = self.me.get_active_element()
        print(a)

    def Move_the_mouse_toEleement_click(self):
        self.me.Move_the_mouse_toEleement_click("XPATH", Mobile_Test.a3)
        self.me.click("ACCESSIBILITY_ID", Mobile_Test.a2)
        print("single click")
    
    def Move_the_mouse_toEleement_double_Click(self):
        self.me.Move_the_mouse_toEleement_double_click("XPATH", Mobile_Test.a6)
        print("double click")

    def Move_the_mouse_toEleement_click_and_Hold(self):
        self.me.Move_the_mouse_toEleement_click_and_hold("XPATH", Mobile_Test.a6)
        print("click and hold")

    def Move_the_mouse_toEleement_Release(self):
        self.me.Move_the_mouse_toEleement_release("XPATH", Mobile_Test.a6)
        print("click, hold and release")

    def Move_the_Mouse_by_an_offset(self):
        self.me.Move_the_mouse_by_an_offset()

    def Move_the_mouse_toeleement_SubElement_click(self):
        self.me.Move_the_mouse_toEleement_SubElement_click()

    def single_Tap_element(self):
        self.me.single_tap_element("XPATH", Mobile_Test.a3)
        print("single tap")

    def double_Tap_element(self):
        self.me.single_tap_element("XPATH", Mobile_Test.a3)
        self.me.double_tap_element("XPATH", Mobile_Test.a4)
        print("double tap")

    def finger_Press_and_move(self):
        self.me.click("ACCESSIBILITY_ID", Mobile_Test.a2)
        time.sleep(2)
        self.me.finger_press_and_move("XPATH", Mobile_Test.touch, 20,1000)
        time.sleep(5)

    def Finger_press_move_Release(self):
        self.me.finger_press_move_Release("XPATH", Mobile_Test.touch, 50,1500)

    def finger_Long_Press(self):
        self.me.finger_long_Press("XPATH", Mobile_Test.a3, 10)

    def finger_Touch_scroll(self):
        self.me.click("ACCESSIBILITY_ID", Mobile_Test.a2)
        self.me.finger_touch_scroll("XPATH", Mobile_Test.touch,Mobile_Test.touch1)

    def finger_Touch_flick(self):
        self.me.finger_touch_flick(100, 100, 100, 400)

    def finger_Multi_TouchAction(self):
        self.me.finger_Multi_touchAction(100, 100, 100, 400)
        
    def open_window(self):
        self.me.execute_Script("window.open()")

    def navigate_url(self, url):
        self.u.navigateto(url)
    
    def Switch_toWindoW(self, windowNumber):
        time.sleep(2)
        self.br.switchtoWindowUsingHandle(windowNumber)
        
    def goto_Url(self, url):
        # self.me.execute_Script("window.open()")
        self.me.goto_url(url)
        time.sleep(5)

    def maximize_Window(self):
        self.me.maximize_window()

    def close_Window(self):
        self.me.close_window()
        time.sleep(2)

    def Get_current_window_handle(self):
        a = self.me.get_current_window_handle()
        print(a)

    def Get_all_window_handles(self):
        a = self.me.get_all_window_handles()
        print(a)

    def Get_title(self):
        a = self.me.get_title()
        print(a)

    def Get_windowSize_Dimensions(self):
        a = self.me.get_windowSize_Dimensions()
        print(a)

    def Get_window_position(self):
        a = self.me.get_window_position()
        print(a)
    
    def Get_current_url(self):
        a = self.me.get_current_url()
        print(a)

    def Get_cookies(self):
        a = self.me.get_cookies()
        print(a)

    def Set_window_position(self):
        self.me.set_window_position(10, 10, '0')

    def click_sign_up(self):
        self.u.click(Mobile_Test.w2)

    def enter_text(self):
        self.u.fillField(Mobile_Test.w4,"sreenivas")
        self.u.fillField(Mobile_Test.w5,"reddy")
        time.sleep(2)
        self.u.click(Mobile_Test.w6)

    def click_window(self):
        self.u.click(Mobile_Test.w3)
        self.me.switch_toWindow

    def Navigate_back(self):
        self.me.navigate_back()

    def Navigate_forward(self):
        self.me.navigate_forward()

    def Refresh_current_page(self):
        self.me.refresh_current_page()

    def set_Cookies(self):
        self.me.set_cookies({'foo', 'bar'})
        time.sleep(15)

    def Delete_cookie(self):
        self.me.delete_cookie('foo')
        time.sleep(5)

    def Delete_All_cookie(self):
        self.me.delete_All_cookie()

    def Switchto_Frame(self):
        # self.me.switchTo_Frame(7)
        self.br.switchToFrame(Mobile_Test.frame1)

    def enter_email_frame(self):
        self.u.fillField(Mobile_Test.w7, "sreenivashs38@gmail.com")

    def Switch_to_parent_frame(self):
        self.br.switchToParentFrame()
        print("switch to parent")

    # def click_signup(self):
    #     self.u.actionClick(Mobile_Test.w8)

    def Switch_to_frame_name(self):
        self.br.switch_To_Frame_ByName("newsletter-signup-form")
    
    def enter_email_frame(self):
        self.u.fillField(Mobile_Test.w7, "sreenivashs38@gmail.com")

    def Driver_execute_async_script(self):
        self.me.driver_execute_async_script(Mobile_Test.script)

    def isApp_Installed(self):
        self.mobAppium.isApp_installed('com.airbnb.android')

    def Launch_app(self):
        self.mobAppium.Launch_App()
        time.sleep(5)

    def sendApp_To_background(self):
        self.mobAppium.sendApp_To_Background()

    def close_app(self):
        self.mobAppium.close_App()

    def reset_app(self):
        self.mobAppium.reset_App()

    def Removeapp(self):
        self.mobAppium.RemoveApp('com.google.android.apps.youtube.music')

    def activate_app(self):
        self.mobAppium.activate_App('com.google.android.apps.youtube.music')

    def Terminate_app(self):
        self.mobAppium.Terminate_App('com.google.android.apps.youtube.music')
        time.sleep(5)

    def shake_Device(self):
        self.mobAppium.shake_device()

    def Lock_device(self):
        self.mobAppium.lock_device()

    def Unlock_device(self):
        self.mobAppium.unlock_device()

    def isDevice_LockeD(self):
        self.mobAppium.isDevice_Locked()

    def press_Key_Code(self):
        self.mobAppium.press_Key_code(10)

    def Logng_press_Key_code(self):
        self.mobAppium.Logng_press_Key_code(10)

    def Hide_Key_board(self):
        self.mobAppium.Hide_Key_Board()

    def Is_Keyboard_Shown(self):
        self.mobAppium.is_keyboard_Shown()
        assert True

    def key_event(self):
        self.mobAppium.key_Event(10)

    def toggle_Wifi_service(self):
        self.mobAppium.toggle_wifi_Service()

    def toggle_locatioN_services(self):
        self.mobAppium.toggle_location_Services()

    def send_SmsEemulatorOnly(self):
        self.mobAppium.send_sms_emulatorOnly('555-123-4567', 'Hey lol')

    def make_GSM_call_EmulatorOnlY(self):
        self.mobAppium.make_GSM_call_emulatorOnly("5551234567",'call')
        time.sleep(5)

    def set_GSM_Signal_strength_emulatorOnly(self):
        self.mobAppium.set_GSM_signal_strength_emulatorOnly(2)
        time.sleep(5)

    def Set_GSM_signal_emulatorOnly(self):
        self.mobAppium.set_GSM_signal_emulatorOnly('home')
        time.sleep(5)

    def set_Network_speed_emulatorOnly(self):
        self.mobAppium.set_network_speed_emulatorOnly('lte')

    def get_performance_data(self):
        a = self.mobAppium.get_performance_Data(('com.airbnb.android', 'batteryinfo', 10))
        print(a)

    def get_performance_Data_Types(self):
        a = self.mobAppium.get_performance_data_Types()
        print(a)

    def start_Recording_Screen(self):
        self.mobAppium.start_recording_Screen()
        time.sleep(5)

    def stop_Recording_Screen(self):
        self.mobAppium.stop_recording_Screen()

    def Get_pageSource(self):
        a = self.mobAppium.get_PageSource()
        print(a)

    def Get_Orientation(self):
        a = self.mobAppium.get_Orientation()
        print(a)

    def get_GeoLocation(self):
        a = self.mobAppium.get_geoLocation()
        print(a)


    def getLog_types(self):
        a = self.mobAppium.getLog_Types()
        print(a)

    def Get_Clipboard(self):
        a = self.mobAppium.get_Clipboard()
        print(a)

    def Get_ClipboardTest(self):
        a = self.mobAppium.get_ClipboardTest()
        print(a)

    def Set_ClipBoard(self):
        self.mobAppium.set_ClipBoard(b'blue')

    def Set_Clipboard_Text(self):
        self.mobAppium.set_Clipboard_Text(b'blue')

    def Set_Power_Ac_forEmulator(self):
        self.mobAppium.Set_Power_ac_forEmulator('on')

    def set_Power_capacity_forEmulator(self):
        self.mobAppium.set_power_capacity_forEmulator(30)

    def Log_event(self):
        self.mobAppium.Log_Event('appium', 'funEvent')

    def Get_event(self):
        a = self.mobAppium.Get_Event('appium')
        print(a)

    def Update_settingS(self):
        self.mobAppium.Update_Settings(["ignoreUnimportantViews : true"])

    def Get_Settings(self):
        self.mobAppium.Get_settings()

    def execute_driver(self):
        self.mobAppium.execute_Driver(Mobile_Test.scripts)

    def open_Notifications_andriod_emulatorOnly(self):
        self.mobAppium.open_notifications_andriod_emulatorOnly()

    def Get_system_Bars(self):
        a = self.mobAppium.get_system_Bars()
        print(a)

    def get_Device_Time(self):
        a = self.mobAppium.get_device_Time()
        print(a)

    def get_Display_density_android(self):
        a = self.mobAppium.get_display_density_android()
        print(a)

    def Finger_print_android_emulator(self):
        self.mobAppium.finger_print_android_emulator(1)

    def Set_Orientation(self):
        self.mobAppium.set_Orientation("LANDSCAPE")


    def get_Remote_driver_Status(self):
        self.mobAppium.get_Remote_Driver_Status(4723)

    def Execute_Mobile_Command(self):
        self.mobAppium.execute_Mobile_Command("mobile: scroll", {'direction': 'down'})

    def create_newSession(self):
        self.mobAppium.create_NewSession()

    def End_Session(self):
        self.mobAppium.end_Session()

    def Get_Session_Capabilities(self):
        self.mobAppium.get_Session_Capabilities()

    def go_back(self):
        self.mobAppium.go_Back()

    def Take_screenshot(self):
        self.mobAppium.take_screenshot()

    def set_PageLoad_timeout(self):
        self.mobAppium.set_PageLoad_Timeout("1000")

    def set_scriptLoad_timeout(self):
        self.mobAppium.set_scriptLoad_Timeout("1000")

    def set_Implicit_Wait_timeout(self):
        self.mobAppium.set_Implicit_Wait_Timeout("5")

    
    def getlogs(self):
        a = self.mobAppium.getLogs('client')
        print(a)

    def install_App(self):
        self.mobAppium.install_app(r"D:\Users\ssreeenivasreddy\Altimetrik_JCL\pythonseleniumframework\Airbnb_v22.21_apkpure.com.apk")
        print("installed")

    def get_App_State(self):
        self.mobAppium.get_App_state()

    def get_App_Strings(self):
        self.mobAppium.get_app_Strings()

    def End_test_Coverage(self):
        self.mobAppium.End_Test_Coverage()

    def push_file_To_Device_From_location(self):
        self.mobAppium.push_file_To_Device_From_Location("\SDCARD\Documents\push.txt",b"sreenivas")

    def pull_file_from_device(self):
        self.mobAppium.pull_file_from_Device()

    def pull_folder_from_device(self):
        self.mobAppium.pull_folder_from_Device()

    def touch_id_Ios_simulator(self):
        self.mobAppium.touch_id_ios_simulator()

    def toggle_touch_id_enrollment_Ios_simulator(self):
        self.mobAppium.toggle_touch_id_enrollment_ios_simulator()

    