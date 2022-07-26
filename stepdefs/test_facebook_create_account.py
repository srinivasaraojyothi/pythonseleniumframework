from pages.facebook import CreateAccount
import time


def test_create_fb_account(browser):
    CreateAccount(browser).search_url("https://www.facebook.com/")
    CreateAccount(browser).click_create_new_account()
    CreateAccount(browser).enter_first_name("sreenivas")
    CreateAccount(browser).enter_surname("reddy")
    CreateAccount(browser).enter_email("sreenivashs38@gmail.com")
    CreateAccount(browser).enter_password("Sree#123")
    CreateAccount(browser).select_day()
    CreateAccount(browser).select_month()
    CreateAccount(browser).select_year()
    CreateAccount(browser).select_gender()
    CreateAccount(browser).click_signup()



