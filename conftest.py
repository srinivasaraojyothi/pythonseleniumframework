import pytest
import allure
from selenium import webdriver
#from appium import webdriver
import os
import sys
import pytest_bdd
from datetime import datetime
from typing import Union,List
import allure
import ast
import requests
import xlrd
import pandas as pd
import json
import numpy as np
import base64
import tweepy
'''
def pytest_addoption(parser):
    parser.addoption(
        "--b", action="store", default="type1", help="my option: type1 or type2"
    )
    parser.addoption(
        "--e", action="store", default="qc", help="my option: type1 or type2"
    )
    parser.addoption(
        "--t", action="store", default="qc", help="my option: type1 or type2"
    )

@pytest.fixture
def b(request):
    return request.config.getoption("--b")
@pytest.fixture
def e(request):
    return request.config.getoption("--e")
@pytest.fixture
def t(request):
    return request.config.getoption("--t")    
@pytest.fixture
def browser(b,t,request ):
    
    if(b=="chrome"):
        if(t=="web"):
            opts = webdriver.ChromeOptions()

            opts.add_argument('--disable-gpu')
            
            #browser = webdriver.Chrome("D:/Users/sjyothi/Downloads/chromedriver/chromedriver.exe", options=opts)
            
            browser=webdriver.Remote(
                        command_executor='http://localhost:4444/wd/hub',
                        options=opts,
                        extensions=List[webdriver]
                    )
                    



            yield browser

                # Quit the WebDriver instance for the teardown
            browser.close()
        else:
            
            desired_caps={
                            "platformName": "Android",
                            "automationName":"UiAutomator2",
                            "appium:deviceName": "Pixel_5_API_31",
                            "appium:app": "D:\\Users\\sjyothi\\Repos\\pythonseleniumFramework\\Airbnb_v22.21_apkpure.com.apk",
                            "appium:appPackage": "com.airbnb.android",
                            "appium:appActivity": "com.airbnb.android.feat.homescreen.HomeActivity"
                            }
            #opts = webdriver.ChromeOptions()

            #opts.add_argument('headless')
            
            #driver = webdriver.Chrome("D:/Users/sjyothi/Downloads/chromedriver/chromedriver.exe", options=opts)
            browser=webdriver.Remote(
                        'http://localhost:4723/wd/hub',
                        desired_caps
                    )


            #browser.set_page_load_timeout(5000)
            #browser.set_script_timeout(5000)
            #browser.implicitly_wait(5)
            yield browser

                # Quit the WebDriver instance for the teardown
            browser.quit() 
'''
'''
@pytest.fixture
def crud_call():
    

    
        consumer_key = 'K2C3YKzB54L3WFBDADsQEBFdf'
        consumer_secret_key = 'yHW5htlvtbxxKqRo7LB0XF6xPZ39dEyf2i177mv56gjF0LtcXB'
        key_secret = '{}:{}'.format(consumer_key, consumer_secret_key).encode('ascii')
    # Transform from bytes to bytes that can be printed
        b64_encoded_key = base64.b64encode(key_secret)
        #Transform from bytes back into Unicode
        b64_encoded_key = b64_encoded_key.decode('ascii')
        base_url = 'https://api.twitter.com/'
        auth_url = '{}oauth2/token'.format(base_url)
        auth_headers = {
            'Authorization': 'Basic {}'.format(b64_encoded_key),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        auth_data = {
            'grant_type': 'client_credentials'
        }
        auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
        print(auth_resp.status_code)
        access_token = auth_resp.json()['access_token']
        yield access_token        

'''

'''
#for allure generation with screenshots and for creating rerun failure.txt file. 'do NOT modify it'
@pytest.hookimpl( hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield

    report = outcome.get_result()
    if report.when == 'call':
        nodeid = item.nodeid
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            mode = 'a' if os.path.exists('failures') else 'w'
            try:
                with open('failures', mode) as f:
                    f.write(report.nodeid + "\n")
                    feature_request = item.funcargs['request']
                    #print(feature_request,"report")
                    driver = feature_request.getfixturevalue('browser')
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name='screenshot',
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print('Fail to take screen-shot: {}'.format(e))        


# for all test cases executed, 'do NOT modify it'
@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    yield
    print('this happens after the test runs',pyfuncitem.funcargs['request'].getfixturevalue)
    
    if 'watch_logs' in pyfuncitem.funcargs:
            print(pyfuncitem.funcargs['watch_logs']())




# for html report with screenshots, 'do notmodify it'
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    #monkeypatch 
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    #setattr()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        feature_request = item.funcargs['request']
        #print(feature_request,"report")
        driver = feature_request.getfixturevalue('browser')
        nodeid = item.nodeid
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H_%M")}.png'.replace("/", "_").replace("::", "_").replace(".py", "")
            img_path = os.path.join("D:\\Users\\sjyothi\\Repos\\pythonseleniumFramework\\features", "screenshots", file_name)
            driver.save_screenshot(img_path)
            screenshot = driver.get_screenshot_as_base64() # the hero
            extra.append(pytest_html.extras.image(screenshot, ''))
        report.extra = extra

       
''' 