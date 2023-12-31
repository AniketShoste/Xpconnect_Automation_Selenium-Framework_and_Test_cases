import time

from selenium.webdriver.common.by import By

from pages.base import BaseSetup
from pages.veeva_to_aem_transfer import VeevatoAemContentTransfer
from utils.webdriverutil import WebDriverUtil

'''
This class validates document sent from veeva to AEM.
'''

class ValidateVeevaDocAem(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)

    '''
    Locators and methods of the page written on same page - This is part of page object model
    '''
    home_page_aem = (By.XPATH, "//a[@id='globalNavHeader']/coral-icon[@role='img']")
    folder_asset = (By.CSS_SELECTOR, "[icon='asset']")
    folder_files = (By.CSS_SELECTOR, "[data-foundation-collection-navigator-href] [icon='folder']")
    folder_xpconnect = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='/content/dam/xpconnect'] .coral3-Card-context")
    folder_demovault = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='/content/dam/xpconnect/demo-vault'] .foundation-collection-item-title")
    content_component_asset = (By.CSS_SELECTOR,"coral-masonry-item:nth-of-type(2)  .coral3-Card.foundation-collection-navigator > coral-card-info")
    xp_connect_content = (By.CSS_SELECTOR, "a#xpconnect-trigger > coral-anchorbutton-label")
    v_meta_data = (By.CSS_SELECTOR, "div#pageinfo-data > button[title='Veeva Metadata']")
    document_id_vm = (By.CSS_SELECTOR, "[role='row']:nth-of-type(8) [role='gridcell']:nth-of-type(2)")

    def click_home_page_aem(self):
        self.seleniumutil.wait_for_element_visible(self.home_page_aem)
        self.seleniumutil.click(*self.home_page_aem)
        print("Clicked on AEM Home pge")

    def click_folder_asset(self):
        self.seleniumutil.wait_for_element_visible(self.folder_asset)
        self.seleniumutil.click(*self.folder_asset)
        print("Clicked on Asset Folder")

    def click_folder_files(self):
        self.seleniumutil.wait_for_element_visible(self.folder_files)
        self.seleniumutil.click(*self.folder_files)
        print("Clicked on File Folder")

    def click_folder_xpconnect(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_visible(self.folder_xpconnect)
        self.seleniumutil.click(*self.folder_xpconnect)
        print("Clicked on Xpconnect Folder")

    def click_folder_demovault(self):
        self.seleniumutil.wait_for_element_visible(self.folder_demovault)
        self.seleniumutil.click(*self.folder_demovault)
        print("Clicked on demovault Folder")

    def scroll_content_component_asset(self):
        self.seleniumutil.wait_for_element_presense(self.content_component_asset)
        self.seleniumutil.move_to_element(self.driver.find_element(*self.content_component_asset))
        print("Scrolled the content")


    def click_content_component_asset(self):
        self.seleniumutil.wait_for_element_clickable(self.content_component_asset)
        self.seleniumutil.click(*self.content_component_asset)
        print("Clicked on content sent from veeva")

    def click_xpconnect_menu(self):
        self.seleniumutil.wait_for_element_visible(self.xp_connect_content)
        self.seleniumutil.click(*self.xp_connect_content)
        print("Clicked on xpconnect from menu")

    def click_v_metadata(self):
        self.seleniumutil.wait_for_element_visible(self.v_meta_data)
        self.seleniumutil.click(*self.v_meta_data)
        print("Clicked on veeva metadata")

    def assert_document_id_veeva_to_aem(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_visible(self.document_id_vm)
        doc_id_aem = self.seleniumutil.text(*self.document_id_vm)
        print("Document id captured", doc_id_aem)
        if doc_id_aem in self.propertyutil.get_property("global_id_veeva"):
            return True
        return False
