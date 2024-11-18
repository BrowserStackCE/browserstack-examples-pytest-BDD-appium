from pytest_bdd import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('the Wikipedia app is launched')
def app_launched(driver):
    assert driver is not None, "Driver is not initialized"

@when('the user opens the app')
def open_app(driver):
    time.sleep(3)  # Wait for the app to load

@then('find "search wikipedia" and click the element')
def search_wikipedia(driver):
    search_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
            )
    search_element.click()

@then('send "Browserstack" as input')
def send_input(driver):
    search_input = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
            )
    search_input.send_keys("BrowserStack")
    time.sleep(5)

@then('search results')
def search_results(driver):
    search_results = driver.find_elements(
            AppiumBy.CLASS_NAME, "android.widget.TextView")
            
    if(len(search_results) > 0):
        print("Search results available")
    else:
        print("Search results unavailable")
