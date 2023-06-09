from selenium.webdriver.common.by import By

from pages.base import BaseSetup

'''
This class is transferring content from veeva to aem
'''

class VeevatoAemContentTransfer(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)

    '''
          Locators and methods of the page written on same page - This is part of page object model
    '''
    document_Types = (By.CSS_SELECTOR, "[order='0'] .facetGroupLabel")
    component_asset = (By.CSS_SELECTOR, "li:nth-of-type(3) > .categoryTerm.doc_link.vv-facet-term")
    content_component_asset = (
        By.CSS_SELECTOR,
        "div[name='SunflowerTest'] .mimeTypeBox > .docThumbnail > .doc_preview_thumbnail.img_float_left")
    menu_for_aem_env = (By.CSS_SELECTOR,
                        ".css-14vl23m-childrenCSS-css-css  .css-11eaezd-buttonCSS-buttonCSS-buttonCSS-buttonCSS-buttonCSS-buttonCSS-DropdownMenu-DropdownMenu > .css-1il8e9o-DropdownMenu")
    demo_env = (By.CSS_SELECTOR, "[data-value='dynamicAction\:LifecycleUserAction10']")
    close_page = (By.CSS_SELECTOR, ".closeIFrameTemplate")
    global_doc_id = (By.CSS_SELECTOR, ".docInfoValue-docGlobalId_b")

    def document_types_veeva(self):
        self.seleniumutil.wait_for_element_visible(self.document_Types)
        self.seleniumutil.click(*self.document_Types)
        print("Clicked on document types")

    def component_asset_veeva(self):
        self.seleniumutil.wait_for_element_visible(self.component_asset)
        self.seleniumutil.click(*self.component_asset)
        print("Clicked on component asset")

    def content_component_asset_veeva(self):
        self.seleniumutil.wait_for_element_visible(self.content_component_asset)
        self.seleniumutil.click(*self.content_component_asset)
        print("Clicked on content under component asset")

    def menu_for_aem_env_veeva(self):
        self.seleniumutil.wait_for_element_visible(self.menu_for_aem_env)
        self.seleniumutil.click(*self.menu_for_aem_env)
        print("Clicked on send content from veeva to aem")

    def demo2_env_aem(self):
        self.seleniumutil.wait_for_element_visible(self.demo_env)
        self.seleniumutil.click(*self.demo_env)
        print("Clicked on demo environment")

    def close_page_icon(self):
        self.seleniumutil.wait_for_element_visible(self.close_page)
        self.seleniumutil.click(*self.close_page)
        print("Clicked on close page icon")

    def global_document_id(self):
        self.seleniumutil.wait_for_element_visible(self.global_doc_id)
        global_id_veeva = self.seleniumutil.text(*self.global_doc_id)
        self.propertyutil.set_property("global_id_veeva", global_id_veeva)
        print("Captured global account id",global_id_veeva)
