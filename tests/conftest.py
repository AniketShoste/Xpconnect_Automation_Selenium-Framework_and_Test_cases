
import pytest

from pages.base import BaseSetup
from pages.login_page import LoginPage
from tests.test_scenario import propertyutil
from utils.webdriverutil import WebDriverUtil

'''
This method gets passed in the test classes and gets executed before test steps, This method is used for setting up application and tearing it down
after the execution is over

'''
@pytest.fixture()
def set_up():
    login_page = LoginPage(WebDriverUtil.get_instance().getwebdriver("Chrome"))
    print(login_page)
    base_page = BaseSetup(WebDriverUtil.getwebdriverinstance())
    print(login_page)
    login_page.initiate_url()
    print("Url initiated")
    login_page.enter_username(login_page.propertyutil.get_property("xp_username"))
    login_page.enter_password(login_page.propertyutil.get_property("xp_password"))
    login_page.click_login()
    base_page.new_tab(propertyutil.get_property("veeva_url"))
    base_page.switch_window("veeva")
    login_page.enter_veeva_username(propertyutil.get_property("veeva_username"))
    login_page.click_continue_veeva_login()
    login_page.enter_veeva_password(propertyutil.get_property("veeva_password"))
    login_page.click_veeva_login()
    yield
    login_page.close_browser()

