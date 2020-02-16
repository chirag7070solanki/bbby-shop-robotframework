from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as seleniumtimeout
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from constants import locators
import time


class selenium_functions:

    def set_web_driver_and_launch_site(self, browser_name, url):
        print("In Selenium Functions")
        print(browser_name)
        print(url)
        if browser_name == "chrome":
            print("Trying to launch Chrome browser")
            driver = webdriver.Chrome("/Users/chiragsolanki/Documents/Technical/Automation/Tools/chromedriver")
            driver.maximize_window()
            driver.get(url)
            time.sleep(5)
            selenium_functions.close_io_pop_up_if_present(driver)
            time.sleep(5)
            return driver
        elif browser_name == "firefox":
            print("Trying to launch Firefox browser")

    def quite_webdriver(self, driver):
        driver.quit()

    def wait_till_element_present(self, driver, waittime, identifier, locator):
        wait = WebDriverWait(driver, waittime)
        try:
            element = wait.until(EC.presence_of_element_located((identifier, locator)))
            return element
        except seleniumtimeout:
            print("Element not found even after waiting for " + waittime + seleniumtimeout)

    def is_element_present(self,driver, identifier, locator):
        try:
            driver.find_element(identifier, locator)
            selenium_functions.wait_till_visible(driver,identifier,locator)
            return True
        except Exception as e:
            print("Element is not present - " + e.__str__())
            return False

    def close_io_pop_up_if_present(self, driver):
        if selenium_functions.is_element_present(driver, By.XPATH, locators.xpath_io_pop_up):
            print("IO pop up present")
            selenium_functions.click_element(driver, By.XPATH, locators.xpath_io_pop_up)
            print("IO modal closed")
            selenium_functions.wait_for_some_time(5)


    def wait_till_visible(self, driver, identifier, locator):
        for i in range(1,90):
            if driver.find_element(identifier, locator).size.get("width") > 0 or driver.find_element(identifier, locator).size.get("height") > 0:
                return True

    def click_element(self, driver, identifier, locator):
        if selenium_functions.is_element_present(driver, identifier, locator):
            driver.find_element(identifier, locator).click()
        else:
            raise Exception("Element " + locator + " not found")

    def move_to_element(self, driver, identifier, locator):
        if selenium_functions.is_element_present(driver, identifier, locator):
            try:
                ele = driver.find_element(identifier, locator)
                action = ActionChains(driver)
                action.move_to_element(ele)
                action.perform()
            except Exception as e:
                raise Exception("Something went wrong while moving to element - " + e.__str__())
        else:
            raise Exception(locator + " is not present on this page")

    def wait_for_some_time(self, sec):
        time.sleep(sec)

    def scroll_till_end_then_top(self, driver):
        print("scrolling")

    def scroll_till_element(self, driver, identifier, locator):
        element = driver.find_element(identifier, locator)
        driver.execute_script("arguments[0].scrollIntoView();", element)


selenium_functions = selenium_functions()

