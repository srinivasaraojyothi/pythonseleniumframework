from distutils.command.config import config
from allure_commons.lifecycle import AllureLifecycle
from allure_commons import plugin_manager
from allure_commons.model2 import TestResult
from distutils.log import error
import imp
#from importlib.resources import path
from platform import platform
from this import s
#from cv2 import getDerivKernels
#from matplotlib.pyplot import text
import pytest
import allure
from pytest import CaptureFixture
#import pytest_bdd
#from selenium import webdriver
#from appium import webdriver

import os
import re
import sys

#from pytest_bdd import hooks
from datetime import datetime
from typing import Union, List
from pytest_html import extras, plugin
import allure
import ast
from py.xml import html
import subprocess as sp
from appium.webdriver.appium_service import AppiumService
import requests
#from torch import embedding
#import xlrd
import pandas as pd
import json
import numpy as np
#import base64
import time
#import tweepy
from config import rootPath, summary_modification, anodroidEmulatorSetandStart, appiumStart, chromeBrowser, firefoxBrowser, native_MobileApp_ChromeBrowser, native_MobileApp_FirefoxBrowser, web_MobileApp_ChromeBrowser, web_MobileApp_FirefoxBrowser
from pyallied.web.webWaits import customwebDriverwait


def pytest_addoption(parser):
    parser.addoption(
        "--b", action="store", default="chrome", help="my option: type1 or type2"
    )
    parser.addoption(
        "--e", action="store", default="qc", help="my option: type1 or type2"
    )
    parser.addoption(
        "--t", action="store", default="web", help="my option: type1 or type2"
    )


@pytest.fixture(scope='session')
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
    try:
        browser = ''
        if(t in "web"):

            if(b in "chrome"):

                browser = chromeBrowser()

            if(b in "firefox"):
                browser = firefoxBrowser()

            yield browser

            browser.close()
        if(t in "n_mob"):
            #browser = ''
            if(b == "chrome"):
                browser = native_MobileApp_ChromeBrowser()

            if(b in "firefox"):
                browser = native_MobileApp_FirefoxBrowser()

            yield browser

            browser.quit()
        if(t in "w_mob"):
            #browser = ''
            if(b in "chrome"):
                browser = web_MobileApp_ChromeBrowser()

            if(b in "firefox"):
                browser = web_MobileApp_FirefoxBrowser()
            yield browser

            # Quit the WebDriver instance for the teardown
            browser.quit()
        if("profile" in t):
            file = open(rootPath()+"testdata/executionprofile.json")
            data = json.load(file)[t]
            if(data["browser"] in "chrome"):

                browser = chromeBrowser()

            if(data["browser"] in "firefox"):
                browser = firefoxBrowser()

            yield browser

            browser.close()

    except Exception as error:
        raise error


# for allure generation with screenshots and for creating rerun failure.txt file. 'do NOT modify it'
@pytest.hookimpl(hookwrapper=True)
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
                    # print(feature_request,"report")
                    driver = feature_request.getfixturevalue('browser')
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name='screenshot',
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as e:
                print('Fail to take screen-shot: {}'.format(e))
    #p = sp.Popen('D:/Users/sjyothi/Repos/pythonseleniumFramework/allure-2.18.1/bin/allure.bat generate allurereports  allure-report --clean && D:/Users/sjyothi/Repos/pythonseleniumFramework/allure-2.18.1/bin/allure.bat open -h localhost -p 52399', stdout=sp.PIPE, text=True, shell=True)


# for all test cases executed, 'do NOT modify it'
@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    yield
    print('this happens after the test runs',
          pyfuncitem.funcargs['request'].getfixturevalue)

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
    if "profile"not in t:
        with open(rootPath()+"/env.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            data["env"] = e
            data["browser_name"] = b
            data["test_platform"] = t

            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()
    else:
        file = open(rootPath()+"testdata/executionprofile.json")
        executiondata = json.load(file)[t]
        with open(rootPath()+"/env.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            data["env"] = executiondata["env"]
            data["browser_name"] = executiondata["browser"]
            data["test_platform"] = executiondata["platform"]

            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    with open(rootPath()+"/env.json", "r+") as jsonFile:
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


@pytest.fixture(scope='session', autouse=True)
def setup_appium(platformType, setup_androidVirtualDevice):
    try:
        appiumStart(platformType)

    except Exception as error:
        raise error


@pytest.fixture(scope='session')
def setup_androidVirtualDevice(platformType):
    try:
        anodroidEmulatorSetandStart(platformType,)
    except Exception as error:
        raise error
# @given('screenshot insert')


@pytest.hookimpl()
def pytest_html_results_summary(prefix, summary, postfix):
    summary_modification(prefix, summary, postfix)


def custom_write_test_case(self, uuid=None):
    test_result = self._pop_item(uuid=uuid, item_type=TestResult)
    if test_result:
        if test_result.parameters:
            adj_parameters = []
            for param in test_result.parameters:
                if param.name != '_pytest_bdd_example':
                    # do not include parameters with "_pytest_bdd_example"
                    adj_parameters.append(param)
            test_result.parameters = adj_parameters

        plugin_manager.hook.report_result(result=test_result)


AllureLifecycle.write_test_case = custom_write_test_case

# @pytest.fixture(scope='session', autouse=True)


def session_setup_teardown():
    yield
    print("----")
    p = sp.Popen('D:/Users/sjyothi/Repos/pythonseleniumFramework/allure-2.18.1/bin/allure.bat generate allurereports  allure-report --clean && D:/Users/sjyothi/Repos/pythonseleniumFramework/allure-2.18.1/bin/allure.bat open -h localhost -p 52400', stdout=sp.PIPE, text=True, shell=True)
    #sp.Popen('allure-2.18.1/bin/allure.bat generate allurereports  allure-report', stdout=sp.PIPE, text=True, shell=True)
    print("----", p.communicate())
