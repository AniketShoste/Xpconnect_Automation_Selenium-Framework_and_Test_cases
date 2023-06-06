import time

from selenium.webdriver.common.by import By

from pages.base import BaseSetup

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
    folder_files = (By.CSS_SELECTOR, "coral-masonry-item:nth-of-type(1) > div[role='link'] > coral-icon")
    folder_xpconnect = (By.CSS_SELECTOR,"coral-masonry-item:nth-of-type(10)  .coral3-Card.coral3-Card--inverted.foundation-collection-navigator  coral-card-content > coral-card-propertylist")
    folder_demovault = (By.CSS_SELECTOR,"coral-masonry-item:nth-of-type(1)  .coral3-Card.coral3-Card--inverted.foundation-collection-navigator  coral-card-content > .coral3-Card-context")
    content_component_asset = (By.CSS_SELECTOR,"coral-masonry-item:nth-of-type(14)  .coral3-Card.foundation-collection-navigator > coral-card-info")
    xp_connect_content = (By.CSS_SELECTOR, "a#xpconnect-trigger > coral-anchorbutton-label")
    v_meta_data = (By.CSS_SELECTOR, "div#pageinfo-data > button[title='Veeva Metadata']")
    document_id_vm = (By.CSS_SELECTOR, "tr:nth-of-type(9) > td:nth-of-type(2)")

    def click_home_page_aem(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element(self.home_page_aem)
        self.seleniumutil.click(*self.home_page_aem)
        print("Clicked on AEM Home pge")

    def click_folder_asset(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element(self.folder_asset)
        self.seleniumutil.click(*self.folder_asset)
        print("Clicked on Asset Folder")

    def click_folder_files(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element(self.folder_files)
        self.seleniumutil.click(*self.folder_files)
        print("Clicked on File Folder")

    def click_folder_xpconnect(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element(self.folder_xpconnect)
        self.seleniumutil.click(*self.folder_xpconnect)
        print("Clicked on Xpconnect Folder")

    def click_folder_demovault(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element(self.folder_demovault)
        self.seleniumutil.click(*self.folder_demovault)
        print("Clicked on demovault Folder")

    def click_content_component_asset(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element(self.content_component_asset)
        self.seleniumutil.click(*self.content_component_asset)
        print("Clicked on content sent from veeva")

    def click_xpconnect_menu(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element(self.xp_connect_content)
        self.seleniumutil.click(*self.xp_connect_content)
        print("Clicked on xpconnect from menu")

    def click_v_metadata(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element(self.v_meta_data)
        self.seleniumutil.click(*self.v_meta_data)
        print("Clicked on veeva metadata")

    def click_doc_id_vm(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element(self.document_id_vm)
        doc_idaem = self.seleniumutil.text(*self.document_id_vm)
        print("Document id captured", doc_idaem)

    def click_from_aem_homepage(self):
        self.seleniumutil.click_js("//a[@id='globalNavHeader']/coral-icon[@role='img']")