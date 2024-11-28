import os
import pytest
from appium import webdriver
from pytest_bdd import scenarios
from appium.options.android import UiAutomator2Options
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../steps')))
from steps.test_wikipedia_steps import *

BROWSERSTACK_USERNAME = os.getenv('BROWSERSTACK_USERNAME')
BROWSERSTACK_ACCESS_KEY = os.getenv('BROWSERSTACK_ACCESS_KEY')

scenarios('features/wikipedia.feature')

@pytest.fixture(scope="module")
def driver():
    print("Starting BrowserStack Appium session")
    endpoint_url = "http://{}:{}@hub.browserstack.com/wd/hub".format(BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
    capabilities_options = UiAutomator2Options()
    driver = webdriver.Remote(endpoint_url, options=capabilities_options)
    yield driver
    driver.quit()
    print("Ending BrowserStack Appium session")
