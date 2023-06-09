from selenium.webdriver.common.by import By

from pages.base import BaseSetup

'''
This class verifies the document sent from AEM to veeva is matching with veeva document id.
'''


class VeevatoAem(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)
        print("login page init")

    '''
       Locators and methods of the page written on same page - This is part of page object model
    '''

    all_library = (By.CSS_SELECTOR, "li:nth-of-type(2) > .vv-navbar-link")
    recent_library = (By.CSS_SELECTOR, "[class='0TB000000000102 recent'] .vv_secondary_nav_link")
    asset_from_aem = (
        By.CSS_SELECTOR, "div[name='We.Retail'] .mimeTypeBox > .docThumbnail > .doc_preview_thumbnail.img_float_left")
    document_number_veeva = (By.CSS_SELECTOR, ".docInfoValue-DocumentNumber")

    def click_all_library(self, ):
        self.seleniumutil.wait_for_element_visible(self.all_library)
        self.seleniumutil.click(*self.all_library)
        self.seleniumutil.wait_for_element_visible(self.recent_library)
        self.seleniumutil.click(*self.recent_library)
        print("Clicked on all library")

    def click_content_aem(self):
        self.seleniumutil.wait_for_element_visible(self.asset_from_aem)
        self.seleniumutil.click(*self.asset_from_aem)
        print("CLicked on content from library")


    def assert_document_number(self):
        self.seleniumutil.wait_for_element_visible(self.document_number_veeva)
        doc_id_veeva = self.seleniumutil.text(*self.document_number_veeva)
        assert doc_id_veeva == self.propertyutil.get_property("doc_id")
        print("Document validated successfully")