# from SeleniumLibrary import SeleniumLibrary
from SeleniumLibrary import SeleniumLibrary


# create new class that inherits from Selenium2Library
class CustomSeleniumLibrary(SeleniumLibrary):

    def get_webdriver_instance(self):
        return self._current_browser()


custom_selenium = CustomSeleniumLibrary()

