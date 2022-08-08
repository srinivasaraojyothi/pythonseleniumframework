from distutils.log import error
import imp
from importlib.resources import path
from platform import platform
from this import s
from cv2 import getDerivKernels
from matplotlib.pyplot import text
import pytest
import allure
from pytest import CaptureFixture
import pytest_bdd
#from selenium import webdriver
#from appium import webdriver
import os
import re
import sys
from pytest_bdd import hooks
from datetime import datetime
from typing import Union, List
from pytest_html import extras,plugin
import allure
import ast
from py.xml import html
import subprocess as sp
from appium.webdriver.appium_service import AppiumService
import requests
from torch import embedding
import xlrd
import pandas as pd
import json
import numpy as np
import base64
import time
import tweepy
import config
from pyallied.web.webWaits import customwebDriverwait


def pytest_addoption(parser):
    parser.addoption(
        "--b", action="store", default="chrme", help="my option: type1 or type2"
    )
    parser.addoption(
        "--e", action="store", default="qc", help="my option: type1 or type2"
    )
    parser.addoption(
        "--t", action="store", default="web", help="my option: type1 or type2"
    )


@pytest.fixture(scope='package')
def platformType(request):
    
    return request.config.getoption("--t")
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
def browser(b, t, request):

    if(b == "chrome"):
        if(t == "web"):

            from selenium import webdriver
            from selenium.webdriver.common.by import By
            from selenium.webdriver.remote.errorhandler import ErrorHandler
            opts = webdriver.ChromeOptions()

            opts.add_argument('--disable-gpu')

            browser = webdriver.Chrome(
                "D:/Users/sjyothi/Downloads/chromedriver/chromedriver.exe", options=opts)
            #browser2=webdriver.Firefox("D:/Users/sjyothi/Downloads/chromedriver/chromedriver.exe", options=opts)
            '''
            browser=webdriver.Remote(
                        command_executor='http://localhost:4444/wd/hub',
                        options=opts,
                        extensions=List[webdriver]
                    )
            
                    '''

            customwebDriverwait.customWait = 25
            #print(customwebDriverwait.customWait," = custom wait")
            print(browser, ' ------->desired caps')
            browser.get('https://jqueryui.com/droppable/')
            yield browser

            # Quit the WebDriver instance for the teardown
            browser.close()
        elif(t == "n_mob"):
            from appium import webdriver
            from appium.webdriver.common.touch_action import TouchAction
            from selenium.webdriver.common import utils

            desired_caps = {
                "platformName": "Android",
                "androidInstallTimeout":180000,
                "avdLaunchTimeout":1200000,
                "avdReadyTimeout":1200000, 
                "noReset":"true",
                "automationName": "UiAutomator2",
                "appium:deviceName": "pixelT3",
                "appium:app": "D:\\Users\\sjyothi\\Repos\\apks\\Airbnb_v22.21_apkpure.com.apk",
                "appium:appPackage": "com.airbnb.android",
                "appium:appActivity": "com.airbnb.android.feat.homescreen.HomeActivity",
                'chromedriverExecutableDir ':'D:/Users/sjyothi/Repos/pythonseleniumFramework/testdata',
                'chromedriverChromeMappingFile':"D:/Users/sjyothi/AppData/Roamin/npm/node_modules/appium/node_modules/appium-chromedriver/config/mapping.json",

            }

            browser = webdriver.Remote(
                'http://localhost:4723/wd/hub',
                desired_caps,
            )

            # opts.add_argument('headless')

            #driver = webdriver.Chrome("D:/Users/sjyothi/Downloads/chromedriver/chromedriver.exe", options=opts)

            # browser.set_page_load_timeout(5000)
            # browser.set_script_timeout(5000)
            # utils.is_url_connectable(4725,'---------------------------->')
            yield browser

            # Quit the WebDriver instance for the teardown
            browser.quit()
        elif(t == "w_mob"):
            from selenium import webdriver
            from selenium.webdriver.common.by import By
            from selenium.webdriver.remote.errorhandler import ErrorHandler

            mobile_emu = {
                'platformName': 'Android',
                "automationName": "UiAutomator2",
                "deviceName": "pixel_2",
                'browserName': 'Chrome',
                'chromedriverExecutableDir ':'D:/Users/sjyothi/Repos/pythonseleniumFramework/testdata',
                'chromedriverChromeMappingFile':"D:/Users/sjyothi/AppData/Roamin/npm/node_modules/appium/node_modules/appium-chromedriver/config/mapping.json",

            }

            #opts = webdriver.ChromeOptions()
            #opts.add_experimental_option("mobileEmulation", mobile_emu)
            # opts.add_argument('headless')

            browser = webdriver.Remote(
                command_executor='http://localhost:4725/wd/hub', desired_capabilities=mobile_emu)

            # browser.set_page_load_timeout(5000)
            #browser.set_script_timeout(5000)
            # utils.is_url_connectable(4725,'---------------------------->')
            yield browser

            # Quit the WebDriver instance for the teardown
            browser.quit()

        else:
            print("*******noDriver Selected*********")

    elif(b == "firefox"):
        if(t == "web"):

            from selenium import webdriver
            from selenium.webdriver.common.by import By
            from selenium.webdriver.remote.errorhandler import ErrorHandler
            opts = webdriver.ChromeOptions()

            opts.add_argument('--disable-gpu')

            browser = webdriver.Firefox(
                executable_path=r"D:/Users/sjyothi/Downloads/geckodriver/geckodriver.exe")
            #browser2=webdriver.Firefox("D:/Users/sjyothi/Downloads/chromedriver/chromedriver.exe", options=opts)
            '''
            browser=webdriver.Remote(
                        command_executor='http://localhost:4444/wd/hub',
                        options=opts,
                        extensions=List[webdriver]
                    )
            
                    '''

            customwebDriverwait.customWait = 25
            #print(customwebDriverwait.customWait," = custom wait")
            print(browser, ' ------->desired caps')
            yield browser

            # Quit the WebDriver instance for the teardown
            browser.close()


'''
@pytest.fixture
def crud_call():
    
    
        consumer_key = ''
        consumer_secret_key = ''
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
def pytest_runtest_makereport(item, call):
    # monkeypatch
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    # setattr()
    extra = getattr(report, "extra", [])
    #extra.append(extras.html("<div>Additional HTML</div>"))
    # extra.append(extras.image(config.rootPath()+"/screen1.png"))
    if report.when == "call":
        # print(item.runtest(),'------------user')
        #extra.append(extras.html("<div>Additionals HTML</div>"))
        feature_request = item.funcargs['request']
        #print(item.funcargs['request'], "-----report-------")
        driver = feature_request.getfixturevalue('browser')
        nodeid = item.nodeid
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H_%M")}.png'.replace(
                "/", "_").replace("::", "_").replace(".py", "")
            #img_path = os.path.join("D:\\Users\\sjyothi\\Repos\\pythonseleniumFramework\\features", "screenshots", file_name)
            # driver.save_screenshot(img_path)
            screenshot = driver.get_screenshot_as_base64()  # the hero
            extra.append(pytest_html.extras.image(screenshot, ''))
        report.extra = extra

@pytest.fixture(autouse=True)
def update_env_file(b, t, e):
    with open(config.rootPath()+"/env.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data["env"] = e
        data["browser_name"] = b
        data["test_platform"] = t

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    with open(config.rootPath()+"/env.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        session.config._metadata["browserName"] = data["browser_name"]
        session.config._metadata["environment"] = data["env"]
        session.config._metadata["test_platform"] = data["test_platform"]
        jsonFile.close()


@pytest.hookimpl()
def pytest_html_report_title(report):
    report.title = "My very own title!"
    #print(report,'  report')

@pytest.hookimpl()
def test_extra(extra):
    extra.append(extras.html("<div>Additionalsss HTML</div>"))


@pytest.fixture(scope='package', autouse=True)
def setup_appium(platformType,setup_androidVirtualDevice):
    try:
        if platformType=='w_mob' or platformType=='n_mob':
            #import json
            appium_service = AppiumService()

            '''
            args=['-p', '4725','--log', 'D:/Users/sjyothi/Repos/pythonseleniumFramework/testdata/appium.log','--log-timestamp','true'
            ,'--allow-insecure', 'chromedriver_autodownload'],
            '''
            appium_service.start( args=['-p', str('4723'),'--log', 'D:/Users/sjyothi/Repos/pythonseleniumFramework/testdata/appium.log','--local-timezone','--log-timestamp'
            ],timeout_ms=10000)
            #ele=sp.Popen('avdmanager delete avd -n pixel', stdout=sp.PIPE, text=True, shell=True)
            #print(ele.returncode,'<-----------')
            #time.sleep(20)
            #emulatorStart=sp.Popen('emulator -avd pixelT3 -partition-size 1024 -wipe-data -no-snapshot-load', stdout=sp.PIPE,stderr=sp.STDOUT,shell=True)
            #print("------------------------ele---->",ele,"------------------------ele---->")
            #emulatorStartErr=emulatorStart.communicate()[0]
            #print('--error \n',emulatorStartErr,'\n error')
            print(appium_service.is_running,',Appium service started...')
            print(appium_service.is_listening,',Appium service started listening...')            
            #ele = sp.Popen('avdmanager -s list', stdout=sp.PIPE, text=True, shell=True)
            #for i in ele.stdout.read().splitlines():
            #    print(i)
            time.sleep(80)
            yield appium_service
            appium_service.stop()
        # print('*****SETUP*****')
        else:
            
            yield "not required"
            print(' mobile platform is not selected')

            

    except Exception as error:
        raise error    


@pytest.fixture(scope='package')
def setup_androidVirtualDevice(platformType):
    if platformType=='w_mob' or platformType=='n_mob':
        print('test---')
        '''
        
        shutil.rmtree
        sp.Popen('adb kill-server', stdout=sp.PIPE, text=True, shell=True)
        if(os.path.exists("D:/Users/sjyothi/.android/avd/pixelTest3")):
            pattern= r'D:/Users/sjyothi/.android/avd/**/multiinstance.lock'
            for item in glob.iglob(pattern, recursive=True):
        # delete file
                print("Deleting:", item)
                os.remove(item)
            
        #from subprocess import Popen
        commands = ['adb start-server', 'avdmanager create avd -n pixelT -k "system-images;android-31;google_apis;x86_64" -d 1','emulator -avd pixelT -partition-size 1024 -wipe-data -no-snapshot-load']
        procs = [ sp.Popen(i,shell=True) for i in commands ]
        for p in procs:
            p.wait() 
        '''  
        '''
        deviceStart=sp.Popen('adb devices',stdout=sp.PIPE,stderr=sp.STDOUT,shell=True)
        deviceStartErr=deviceStart.communicate()[0]
        print('--error \n',str(deviceStartErr).replace("\r\n"," "),'\n error')    
        deviceServerStart=sp.Popen('adb start-server', stdout=sp.PIPE,stderr=sp.STDOUT,shell=True)
        deviceServerStartErr=deviceServerStart.communicate()[0]
        print('--error \n',str(deviceServerStartErr).replace("\r\n"," "),'\n error')
        emulatorCreate=sp.Popen('avdmanager create avd -n pixelT3 -k "system-images;android-31;google_apis;x86_64" -d 1 --force', stdout=sp.PIPE,stderr=sp.STDOUT,shell=True)      
        emulatorCreateErr=emulatorCreate.communicate()[0]
        print('--error \n',str(emulatorCreateErr).replace("\r\n"," "),'\n error')
        '''
        emulatorStart=sp.Popen('emulator -avd pixelT3 -partition-size 1024 -wipe-data -no-snapshot-load', stdout=sp.PIPE,stderr=sp.STDOUT,shell=True)
        #print("------------------------ele---->",ele,"------------------------ele---->")
        #emulatorStartErr=emulatorStart.communicate()[0]
        #print('--error \n',str(emulatorStartErr).replace("\r\n"," "),'\n error')
        #if(ele.returncode):
            #print('---')   
            #sp.Popen('adb start-server', stdout=sp.PIPE, text=True, shell=True)
            
            #ele=sp.Popen('avdmanager delete avd -n pixelTest3 --force', stdout=sp.PIPE, text=True, shell=True)
            #print(ele.returncode,'<-----------')
            #time.sleep(20)
            #sp.Popen('avdmanager create avd -n pixelTest3 -k "system-images;android-33;google_apis;x86_64" -d 1 --force', stdout=sp.PIPE, text=True, shell=True)
        #time.sleep(180)
            #start=sp.Popen('emulator -avd pixelTest3 -partition-size 1024 -wipe-data -no-snapshot-load',
                            #stdout=sp.PIPE, text=True, shell=True)
        time.sleep(60)                 
        #ele = sp.Popen('avdmanager -s list', stdout=sp.PIPE, text=True, shell=True)

        #print(ele.returncode)
        #for i in ele.stdout.read().splitlines():
            #print(i)
        #yield start
        #start.kill()
        #sp.Popen(' adb emu kill', stdout=sp.PIPE, text=True, shell=True)
        # print('*****SETUP*****')
#@given('screenshot insert')        
def pytest_bdd_after_scenario(request, feature, scenario):
    print()

@pytest.hookimpl()
def pytest_html_results_summary(prefix, summary, postfix):

    
    summary.extend ([html.p('')])
    #style=html.style(border='1px solid black')
    #table_1 = html.div( class_="pie",style="height: 100px;width:100px;border-radius: 50%;background: conic-gradient(brown 0.00%, black 0.00% 0.55%, blue 0.55% 6.08%, green 6.08% 13.68%, yellow 13.68% 23.27%, orange 23.27% 40.47%, red 40.47%)")
    

    
    pass_testcases=0
    failed_testcase=0
    skipped_testcase=0
    error_testcases=0

    for i in summary:
        #print(i,    '<---loop--')
        
        if 'py._xmlgen.span' in str(type(i)) :
            if '<span class="skipped">' in str(i):
                skipped_testcase=int(re.findall(r'\d+', str(i))[0])
            if '<span class="failed">' in str(i):
                failed_testcase=int(re.findall(r'\d+', str(i))[0])
            if '<span class="passed">' in str(i):
                pass_testcases=int(re.findall(r'\d+', str(i))[0])
            if '<span class="error">' in str(i):
                error_testcases=int(re.findall(r'\d+', str(i))[0])                
    total_cases=pass_testcases+failed_testcase+skipped_testcase


    failed=str((failed_testcase/total_cases))
    passsed=str((pass_testcases/total_cases)) 
     
    skipped=str((skipped_testcase/total_cases)) 
    errorcases=str((error_testcases/total_cases)) 

    data_pie=html.link( rel='stylesheet',href='report_styles/summarypiechart.css')
    data_pie.append(html.div( class_="pie",style="--val_1:"+failed+"; --val_2:"+passsed+"; --val_3:"+skipped+"; --val_4:"+errorcases))
    Data_table=html.div(class_="Container",style="float: right;position: relative;left: -70%;padding: 0 70px;line-height: 200%;")
    Data_table.append(html.ul())
    Data_table.append(html.li("pass %: "+str((pass_testcases/total_cases)*100),style="color: green;font-size: 12px;align-content: center;"))
    Data_table.append(html.li("fail %: "+str((failed_testcase/total_cases)*100),style="color: red;font-size: 12px;align-content: center;"))
    Data_table.append(html.li("skip %: "+str((skipped_testcase/total_cases)*100),style="color: orange;font-size: 12px;align-content: center;"))
    Data_table.append(html.li("error %: "+str((error_testcases/total_cases)*100),style="color: red;font-size: 12px;align-content: center;"))
    summary.extend ([data_pie,Data_table])