
import pytest

from pages.login_page import LoginPage
from utils.webdriverutil import WebDriverUtil

login_page = LoginPage(WebDriverUtil.get_instance().getwebdriver("Chrome"))
print(login_page)

@pytest.fixture()
def set_up():
    print(login_page)
    login_page.initiate_url()
    print("Url initiated")
    login_page.enter_username(login_page.propertyutil.get_property("xp_username"))
    login_page.enter_password(login_page.propertyutil.get_property("xp_password"))
    login_page.click_login()

