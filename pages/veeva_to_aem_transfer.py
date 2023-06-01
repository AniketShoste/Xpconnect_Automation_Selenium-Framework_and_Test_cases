from selenium.webdriver.common.by import By

from pages.base import BaseSetup


class VeevatoAemContentTransfer(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)
        # print("login page init")
        # self.driver = driver
        # self.selenium_utility = SeleniumUtility(self.driver)

    #all_library = (By.CSS_SELECTOR, "li:nth-of-type(2) > .vv-navbar-link")
    document_Types = (By.CSS_SELECTOR, "[order='0'] .facetGroupLabel")
    component_asset = (By.CSS_SELECTOR, "li:nth-of-type(3) > .categoryTerm.doc_link.vv-facet-term")
    content_component_asset = (By.CSS_SELECTOR, "div[name='book'] .mimeTypeBox > .docThumbnail > .doc_preview_thumbnail.img_float_left")
    menu_for_aem_env = (By.CSS_SELECTOR,".css-14vl23m-childrenCSS-css-css  .css-11eaezd-buttonCSS-buttonCSS-buttonCSS-buttonCSS-buttonCSS-buttonCSS-DropdownMenu-DropdownMenu > .css-1il8e9o-DropdownMenu")
    demo_env = (By.CSS_SELECTOR, "[data-value='dynamicAction\:LifecycleUserAction10']")
    close_page = (By.CSS_SELECTOR, ".closeIFrameTemplate")
    global_doc_id = (By.CSS_SELECTOR, ".docInfoValue-docGlobalId_b")

    def document_types_veeva(self):
        self.seleniumutil.wait_for_element(self.document_Types)
        self.seleniumutil.click(*self.document_Types)
        print("Clcked on document types")

    def component_asset_veeva(self):
        self.seleniumutil.wait_for_element(self.component_asset)
        self.seleniumutil.click(*self.component_asset)
        print("Clcked on component asset")

    def content_component_asset_veeva(self):
        self.seleniumutil.wait_for_element(self.content_component_asset)
        self.seleniumutil.click(*self.content_component_asset)
        print("Clcked on content under component asset")

    def menu_for_aem_env_veeva(self):
        self.seleniumutil.wait_for_element(self.menu_for_aem_env)
        self.seleniumutil.click(*self.menu_for_aem_env)
        print("Clcked on send content from veeva to aem")

    def demo2_env_aem(self):
        self.seleniumutil.wait_for_element(self.demo_env)
        self.seleniumutil.click(*self.demo_env)
        print("Clcked on demo environment")

    def close_page_icon(self):
        self.seleniumutil.wait_for_element(self.close_page)
        self.seleniumutil.click(*self.close_page)
        print("Clcked on close page icon")

    def global_document_id(self):
        self.seleniumutil.wait_for_element(self.global_doc_id)
        self.seleniumutil.click(*self.global_doc_id)
        print("Captured global account id")