import time
from datetime import time

from selenium.webdriver.common.by import By

from pages.base import BaseSetup

'''
This class has AEM and Veeva login methods

'''
class LoginPage(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)
        print("login page init")


    username_field = (By.CSS_SELECTOR, "#username")
    password_field = (By.CSS_SELECTOR, "#password")
    login_button = (By.ID, "submit-button")
    veeva_username = (By.ID, "j_username")
    veeva_continue_button = (By.NAME, "continue")
    veeva_password = (By.ID, "j_password")
    veeva_submit = (By.NAME, "login")
    aem_user = (By.CSS_SELECTOR, "coral-shell-menubar-item:nth-of-type(5)  coral-icon[role='img']")
    aem_sign_out = (By.CSS_SELECTOR, "a:nth-of-type(2) > coral-anchorbutton-label")
    '''
    This is generic method to browser any url
    '''
    def browse_url_app(self, url):
        self.seleniumutil.browse_url(url)
        print("Url Entered", url)

    '''
    This method accept username as a parameter and enters the username in AEM username field
    '''

    def enter_username(self, xp_username):
        self.seleniumutil.wait_for_element_visible(self.username_field)
        print(*self.username_field)
        self.seleniumutil.send_keys(*self.username_field, xp_username)
        print("Username entered")

    '''
       This method accept password as a parameter and enters the username in AEM password field
    '''

    def enter_password(self, xp_password):
        self.seleniumutil.wait_for_element_visible(self.password_field)
        self.seleniumutil.send_keys(*self.password_field, xp_password)
        print("Password entered")
    '''
    AEM Login
    '''

    def click_login(self):
        self.seleniumutil.wait_for_element_visible(self.login_button)
        self.seleniumutil.click(*self.login_button)
        print("Button clicked")
    '''
    Veeva username - accepts username as a parameter
    '''

    def enter_veeva_username(self, veeva_username):
        print(*self.username_field)
        self.seleniumutil.send_keys(*self.veeva_username, veeva_username)
        print("Veeva Username entered")
    '''
    continue button after veeva username 
    '''

    def click_continue_veeva_login(self):
        self.seleniumutil.click(*self.veeva_continue_button)
        print("Veeva continue username ")

    '''
    Entered veeva password 
    '''

    def enter_veeva_password(self, veeva_password):
        self.seleniumutil.wait_for_element_visible(self.veeva_password)
        self.seleniumutil.send_keys(*self.veeva_password, veeva_password)
        print("Veeva Password entered")

    '''
    click veeva login 
    '''

    def click_veeva_login(self):
        self.seleniumutil.wait_for_element_visible(self.veeva_submit)
        self.seleniumutil.click(*self.veeva_submit)
        print("Veeva logged in ")

    ''''
    Close browser method
    
    '''


    def close_browser(self):
        self.seleniumutil.close_browser()
        print("Browser closed")

    ''''
    AEM sign out method
    
    '''

    def click_aem_sign_out(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element_visible(self.aem_user)
        self.seleniumutil.click(*self.aem_user)
        self.seleniumutil.wait_for_element_visible(self.aem_sign_out)
        self.seleniumutil.click(*self.aem_sign_out)
        print("AEM Signed out")
