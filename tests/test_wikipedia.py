import os
import pytest
from appium import webdriver
from pytest_bdd import scenarios
from appium.options.android import UiAutomator2Options
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../steps')))
from steps.test_wikipedia_steps import *


BROWSERSTACK_USERNAME = os.getenv('BROWSERSTACK_USERNAME')
BROWSERSTACK_ACCESS_KEY = os.getenv('BROWSERSTACK_ACCESS_KEY')

scenarios('features/wikipedia.feature')


@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        "platformName": "Android", 
        "platformVersion": "13.0", 
        "deviceName": "Samsung Galaxy S23",  
        "app": "bs://<app-id>", 
        "automationName": "UiAutomator2", 
        "appiumVersion": "1.22.0",  
        "project": "Wikipedia App Tests",
        "build": "Build-1",
        "name": "Wikipedia App BDD Test"
    }
    print("Starting BrowserStack Appium session")
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    endpoint_url = "http://{}:{}@hub.browserstack.com/wd/hub".format(BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
    driver = webdriver.Remote(endpoint_url, options=capabilities_options)
    yield driver
    driver.quit()
    print("Ending BrowserStack Appium session")

