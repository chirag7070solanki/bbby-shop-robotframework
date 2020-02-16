from utilities.selenium_functions import selenium_functions
from selenium.webdriver.common.by import By
from constants import locators


class HomePage:

    # def close_io_pop_up_if_present(driver):
    #     if selenium_functions.is_element_present(driver, By.XPATH, locators.xpath_io_pop_up):
    #         print("IO pop up present")
    #         selenium_functions.click_element(driver, By.XPATH, locators.xpath_io_pop_up)
    #         print("IO modal closed")
    #         selenium_functions.wait_for_some_time(5)

    def navigate_to_l0(driver, l0_name):
        print("Navigating to L0")
        if l0_name == "Categories":
            if selenium_functions.is_element_present(driver, By.XPATH, locators.xpath_lo_products):
                selenium_functions.click_element(driver, By.XPATH, locators.xpath_lo_products)
                selenium_functions.wait_for_some_time(5)

    def navigate_to_l1(driver, action, l1_category):
        print("Navigating to L1")
        print(driver)
        print(l1_category)
        xpathl1 = "//section[contains(@class,'MenuPanel')]//div[text()='Categories']/following-sibling::a[text()='" + l1_category + "']"
        if selenium_functions.is_element_present(driver, By.XPATH, xpathl1):
            if action == "move to":
                selenium_functions.move_to_element(driver, By.XPATH, xpathl1)
                selenium_functions.wait_for_some_time(5)
            elif action == "click":
                selenium_functions.click_element(driver, By.XPATH, xpathl1)
                selenium_functions.wait_for_some_time(5)
        else:
            raise Exception(l1_category + " is not present in flyout")

    def navigate_to_l2(driver, action, l1_category, l2_category):
        print("Navigating to L2")
        xpathl2 = "//*[@id='top-nav-menu']/div[1]//div[contains(@class,'MegaMenu')]/section/div[1]/div[1]/a[contains(" \
                  "text(),'" + l1_category + "')]/following-sibling::section/div/div/a[@data-locator=\"" + l2_category + \
                  "_menuLink\"] "
        if selenium_functions.is_element_present(driver, By.XPATH, xpathl2):
            if action == "move to":
                selenium_functions.move_to_element(driver, By.XPATH, xpathl2)
                selenium_functions.wait_for_some_time(5)
            elif action == "click":
                selenium_functions.click_element(driver, By.XPATH, xpathl2)
                selenium_functions.wait_for_some_time(5)
        else:
            raise Exception(l2_category + " is not present in flyout")


homepage = HomePage()

