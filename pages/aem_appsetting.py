import time

from selenium.webdriver.common.by import By

from pages.base import BaseSetup

'''
This class is transferring content from veeva to aem
'''


class AEM_Appsetting(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)

    '''
          Locators and methods of the page written on same page - This is part of page object model
    '''
    xpconnect_content = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='\/content\/XpConnect']")
    xp_appsetting = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='\/content\/XpConnect\/application-settings'] coral-columnview-item-thumbnail")
    xp_edit_button = (By.CSS_SELECTOR, "coral-actionbar-item:nth-of-type(2)  coral-button-label")
    frame_demo = (By.CSS_SELECTOR, "iframe#ContentFrame")
    demo_dashboard = (By.CSS_SELECTOR,".navbar-nav.mr-auto > .nav-item:nth-child(3) .nav-link")
    veeva_credentials = (By.CSS_SELECTOR,".container > .title")
    fetch_veeva_url = (By.CSS_SELECTOR,"input#credentialsVaultURI")
    fetch_veeva_username = (By.CSS_SELECTOR,"input#credentialsUsername")



    def click_xpconnect_content(self):
        self.seleniumutil.wait_for_element_visible(self.xpconnect_content)
        self.seleniumutil.click(*self.xpconnect_content)
        print("Click on Xpconnect from AEM")

    def click_app_setting(self):
        self.seleniumutil.wait_for_element_visible(self.xp_appsetting)
        self.seleniumutil.click(*self.xp_appsetting)
        print("Click on Xpconnect application setting")

    def click_xp_edit_button(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element_clickable(self.xp_edit_button)
        self.seleniumutil.click(*self.xp_edit_button)
        print("Click on Xpconnect application setting")

    def switch_to_appsetting_frame(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element_visible(self.frame_demo)
        self.seleniumutil.switch_to_frame(*self.frame_demo)
        print("Switched frame")

    def click_demo_dashboard(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element_visible(self.demo_dashboard)
        self.seleniumutil.click_using_js(*self.demo_dashboard)
        print("Clicked on demo dashboard")
    def click_veeva_credentials(self):
        self.seleniumutil.wait_for_element_visible(self.veeva_credentials)
        print("Waited for element")
        self.seleniumutil.click_using_js(*self.veeva_credentials)
        print("clicked on veeva credentails")

    def verify_veeva_url(self):
        self.seleniumutil.wait_for_element_visible(self.fetch_veeva_url)
        veevaurl = self.seleniumutil.fetch_using_js(*self.fetch_veeva_url)
        self.propertyutil.set_property("veeva_url_validate", veevaurl)
        print("Captured veeva url from application setting", veevaurl)

    def verify_veeva_username(self):
        self.seleniumutil.wait_for_element_visible(self.fetch_veeva_username)
        veevausername = self.seleniumutil.fetch_using_js(*self.fetch_veeva_username)
        self.propertyutil.set_property("veeva_username_validate", veevausername)
        print("Captured veeva username from application setting", veevausername)

    def assert_veeva_url_username(self):
        assert self.propertyutil.get_property("v_url_appsetting") == self.propertyutil.get_property("veeva_url_validate")
        assert self.propertyutil.get_property("veeva_username") == self.propertyutil.get_property("veeva_username_validate")
        print("Validation successful")