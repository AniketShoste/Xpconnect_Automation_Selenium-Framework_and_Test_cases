import time
from datetime import time

from selenium.webdriver.common.by import By

from pages.base import BaseSetup


class LoginPage(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)
        print("login page init")
        # self.driver = driver
        # self.selenium_utility = SeleniumUtility(self.driver)

    username_field = (By.CSS_SELECTOR, "#username")
    password_field = (By.CSS_SELECTOR, "#password")
    login_button = (By.ID, "submit-button")
    veeva_username = (By.ID, "j_username")
    veeva_continue_button = (By.NAME, "continue")
    veeva_password = (By.ID, "j_password")
    veeva_submit = (By.NAME, "login")
    aem_user = (By.CSS_SELECTOR, "coral-shell-menubar-item:nth-of-type(5)  coral-icon[role='img']")
    aem_sign_out = (By.CSS_SELECTOR, "a:nth-of-type(2) > coral-anchorbutton-label")

    def browse_url_app(self, url):
        self.seleniumutil.browse_url(url)
        print("Url Entered", url)

    def enter_username(self, xp_username):
        self.seleniumutil.wait_for_element(self.username_field)
        print(*self.username_field)
        self.seleniumutil.send_keys(*self.username_field, xp_username)
        print("Username entered")

    def enter_password(self, xp_password):
        self.seleniumutil.wait_for_element(self.password_field)
        self.seleniumutil.send_keys(*self.password_field, xp_password)
        print("Password entered")

    def click_login(self):
        self.seleniumutil.wait_for_element(self.login_button)
        self.seleniumutil.click(*self.login_button)
        print("Button clicked")

    def enter_veeva_username(self, veeva_username):
        print(*self.username_field)
        self.seleniumutil.send_keys(*self.veeva_username, veeva_username)
        print("Veeva Username entered")

    def click_continue_veeva_login(self):
        self.seleniumutil.click(*self.veeva_continue_button)
        print("Veeva continue username ")

    def enter_veeva_password(self, veeva_password):
        self.seleniumutil.wait_for_element(self.veeva_password)
        self.seleniumutil.send_keys(*self.veeva_password, veeva_password)
        print("Veeva Password entered")

    def click_veeva_login(self):
        self.seleniumutil.wait_for_element(self.veeva_submit)
        self.seleniumutil.click(*self.veeva_submit)
        print("Veeva logged in ")

    def close_browser(self):
        self.seleniumutil.close_browser()
        print("Browser closed")

    def click_aem_sign_out(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element(self.aem_user)
        self.seleniumutil.click(*self.aem_user)
        self.seleniumutil.wait_for_element(self.aem_sign_out)
        self.seleniumutil.click(*self.aem_sign_out)
        print("AEM Signed out")
