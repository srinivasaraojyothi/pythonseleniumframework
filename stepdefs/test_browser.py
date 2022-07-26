from pages.browser_test import Setup

def test_brow(browser):

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
    Setup(browser).Execut_async_Script()
    Setup(browser).close_Driver()


    # Setup(browser).Get_credentials()
    # Setup(browser).Get_Virtual_Authenticator_id()
    # Setup(browser).Print_page()
    # Setup(browser).Remove_all_Credentials()
    # Setup(browser).Remove_Credential()
    # Setup(browser).Remove_Virtual_authenticator()
    # Setup(browser).Set_User_Verified()
    # Setup(browser).Start_Client()
    # Setup(browser).Start_Session()
    # Setup(browser).Stop_Client()
    # Setup(browser).start_Service()
    # Setup(browser).stop_Service()








