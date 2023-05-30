from pages.base import BaseSetup
from selenium.webdriver.common.by import By


class VeevatoAem(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)
        print("login page init")
        # self.driver = driver
        # self.selenium_utility = SeleniumUtility(self.driver)

    all_library = (By.CSS_SELECTOR,"li:nth-of-type(2) > .vv-navbar-link")
    recent_library = (By.CSS_SELECTOR,"[class='0TB000000000102 recent'] .vv_secondary_nav_link")
    asset_from_aem = (By.CSS_SELECTOR, "div[name='We.Retail'] .mimeTypeBox > .docThumbnail > .doc_preview_thumbnail.img_float_left")
    document_number_veeva = (By.CSS_SELECTOR,".docInfoValue-DocumentNumber")

    def click_all_library(self, ):
        self.seleniumutil.wait_for_element(self.all_library)
        self.seleniumutil.click(*self.all_library)
        self.seleniumutil.wait_for_element(self.recent_library)
        self.seleniumutil.click(*self.recent_library)
        print("Clicked on all library")

    def click_content_aem(self):
        self.seleniumutil.wait_for_element(self.asset_from_aem)
        self.seleniumutil.click(*self.asset_from_aem)
        print("CLicked on content from library")

    # def document_number_content(self):
    #     time.sleep(5)
    #     self.seleniumutil.wait_for_element(self.document_number_veeva)
    #     print("Document id from veeva", doc_id_veeva)

    def assert_document_number(self):
        self.seleniumutil.wait_for_element(self.document_number_veeva)
        doc_id_veeva = self.seleniumutil.text(*self.document_number_veeva)
        assert doc_id_veeva == self.propertyutil.get_property("doc_id")
