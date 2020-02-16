from utilities import selenium_functions
from pageobjects import homepage, plppage
from unittest.case import expectedFailure
from ddt import data, unpack, ddt, idata
import unittest
import pytest
import allure
import os
import nose


def data_generator():
    category_data = (('Bath', 'Bath Ru'), ('Bath', 'Bath Towels'))
    for tp1 in category_data:
        yield tp1


@ddt
class PlpLoading(unittest.TestCase):

    def setUp(self):
        print("Set up in progress")
        self.driver = selenium_functions.set_web_driver_and_launch_site("chrome", "https://bedbathandbeyond.com")

    @expectedFailure
    @idata(data_generator())
    @unpack
    def test_test_01(self, l1_category, l2_category):
        print(l1_category)
        print(l2_category)

        homepage.close_io_pop_up_if_present(self.driver)
        homepage.navigate_to_l0(self.driver, "Products")

        homepage.navigate_to_l1(self.driver, "move to", l1_category)
        homepage.navigate_to_l2(self.driver, "click", l1_category, l2_category)
        plppage.check_per_page_sort(self.driver)
        plppage.check_if_product_grid_displayed(self.driver)

    def tearDown(self):
        print("Test complete, cleaning up now!")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
