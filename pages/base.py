import time

from utils.property_util import PropertyUtils
from utils.selenium_utility import SeleniumUtility

'''
Initialize webdriver and url of an application.
'''


class BaseSetup:
    def __init__(self, driver):
        print("driver for base class", driver)
        self.driver = driver
        self.seleniumutil = SeleniumUtility(self.driver)
        self.propertyutil = PropertyUtils()
        print("base set up init")

    def initiate_url(self):
        print("PROPERTY", self.propertyutil.get_property("xp_url"))
        self.seleniumutil.browse_url(self.propertyutil.get_property("xp_url"))
        print("Initiating Url", self.propertyutil.get_property("xp_url"))

    def new_tab(self, url):
        self.seleniumutil.open_new_tab(url)
        print("new tab opened")
        time.sleep(5)

    def switch_window(self, windowtitle):
        self.seleniumutil.switch_to_window(windowtitle)
        print("Switch to window")
        time.sleep(5)

    def refresh_page(self):
        self.seleniumutil.refresh()
