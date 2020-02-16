from utilities.selenium_functions import selenium_functions
from selenium.webdriver.common.by import By
from constants import locators


class PlpPage:

    def check_per_page_sort(self, driver):
        if selenium_functions.is_element_present(driver, By.XPATH, locators.xpath_PLP_perpage_sort):
            print("Per Page Sort option available")
        else:
            raise Exception("Per Page Sort option not displayed")

    def check_if_product_grid_displayed(self, driver):
        if selenium_functions.is_element_present(driver, By.XPATH, locators.xpath_PLP_product_title):
            selenium_functions.scroll_till_element(driver, By.XPATH, locators.xpath_plp_region3)
            selenium_functions.wait_for_some_time(5)
            elements = driver.find_elements(By.XPATH, locators.xpath_PLP_product_title)
            print("Number of products on PLP:" + str(len(elements)))
        else:
            raise Exception("Product grid is not loaded")


plp = PlpPage()

