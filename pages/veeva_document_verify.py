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

    document_number_veva = (By.CSS_SELECTOR, "[docidx='0'] .docNumber")
    document_pdf_veva = (By.CSS_SELECTOR, "div[name='Español'] .mimeTypeBox > .docThumbnail > .doc_preview_thumbnail.img_float_left")
    document_pdf_no_veva = (By.CSS_SELECTOR, ".docInfoValue-DocumentNumber")

    doc_home = (By.CSS_SELECTOR,"div[name='Home'] .mimeTypeBox > .docThumbnail > .doc_preview_thumbnail.img_float_left")
    document_home_number = (By.CSS_SELECTOR, ".docInfoValue-DocumentNumber.doc_info_property_value.vv_docinfo_value")
    document_email_page = (By.CSS_SELECTOR, "div[name='Email Page'] .mimeTypeBox > .docThumbnail > .doc_preview_thumbnail.img_float_left")
    document_demo_website = (By.CSS_SELECTOR, "div[name='Demo Web site'] .mimeTypeBox > .docThumbnail > .doc_preview_thumbnail.img_float_left")
    document_demo_number = (By.CSS_SELECTOR, ".docInfoValue-DocumentNumber.doc_info_property_value.vv_docinfo_value")
    asset_from_aem_editor = (By.CSS_SELECTOR, "div[name='WKND Events'] .docLink.doc_link_large.vv_doc_title_link > .docName.vv_doc_title_name.vv_keep_whitespace")
    xf_from_aem_editor = (By.CSS_SELECTOR, "div[name='Test1'] .docLink.doc_link_large.vv_doc_title_link > .docName.vv_doc_title_name.vv_keep_whitespace")

    doc_first_level = (By.CSS_SELECTOR,"div[name='Language Masters'] .docLink.doc_link_large.vv_doc_title_link > .docName.vv_doc_title_name.vv_keep_whitespace")
    doc_second_level = (By.CSS_SELECTOR,"div[name='English'] .docLink.doc_link_large.vv_doc_title_link > .docName.vv_doc_title_name.vv_keep_whitespace")
    doc_third_level = (By.CSS_SELECTOR,"div[name='Experience'] .docLink.doc_link_large.vv_doc_title_link > .docName.vv_doc_title_name.vv_keep_whitespace")
    doc_fourth_level = (By.CSS_SELECTOR,"div[name='Arctic Surfing In Lofoten'] .docLink.doc_link_large.vv_doc_title_link > .docName.vv_doc_title_name.vv_keep_whitespace")

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
        if doc_id_veeva == self.propertyutil.get_property("doc_id"):
            return True
        return False

    def click_doc_pdf_sent(self):
        self.seleniumutil.wait_for_element_visible(self.document_pdf_veva)
        self.seleniumutil.click(*self.document_pdf_veva)
        print(" PDF Doc is CLicked ")

    def assert_documunet_pdf_no(self):
        self.seleniumutil.wait_for_element_visible(self.document_number_veeva)
        doc_pdf = self.seleniumutil.text(*self.document_number_veeva)
        if doc_pdf == self.propertyutil.get_property("doc_pdf_no"):
            return True
        return False


    def click_doc_home(self):
        self.seleniumutil.wait_for_element_visible(self.doc_home)
        self.seleniumutil.click(*self.doc_home)
        print(" Home Doc is CLicked ")


    def assert_home_no(self):
        self.seleniumutil.wait_for_element_visible(self.document_home_number)
        home_no = self.seleniumutil.text(*self.document_home_number)
        if home_no == self.propertyutil.get_property("home_no"):
            return True
        return False

    def click_doc_email_sent(self):
        self.seleniumutil.wait_for_element_clickable(self.document_email_page)
        self.seleniumutil.click(*self.document_email_page)
        print(" Email Doc is CLicked ")

    def assert_documunet_email_no(self):
        self.seleniumutil.wait_for_element_visible(self.document_number_veeva)
        doc_pdf = self.seleniumutil.text(*self.document_number_veeva)
        if doc_pdf == self.propertyutil.get_property("email_content_id"):
            return True
        return False

    def click_doc_demo_website(self):
        self.seleniumutil.wait_for_element_clickable(self.document_demo_website)
        self.seleniumutil.click(*self.document_demo_website)
        print(" Demo Website Doc is CLicked ")

    def assert_demo_no(self):
        self.seleniumutil.wait_for_element_visible(self.document_demo_number)
        demo_no = self.seleniumutil.text(*self.document_demo_number)
        if demo_no == self.propertyutil.get_property("demo_no"):
            return True
        return False

    def click_content_aem_editor(self):
        self.seleniumutil.wait_for_element_visible(self.asset_from_aem_editor)
        self.seleniumutil.click(*self.asset_from_aem_editor)
        print("CLicked on content from library")

    def click_xf_aem_editor(self):
        self.seleniumutil.wait_for_element_visible(self.xf_from_aem_editor)
        self.seleniumutil.click(*self.xf_from_aem_editor)
        print("CLicked on content from library")

    def assert_document_pdf_number(self):
        self.seleniumutil.wait_for_element_visible(self.document_number_veeva)
        doc_number_pdf = self.seleniumutil.text(*self.document_number_veeva)
        print("Document in Veeva",doc_number_pdf)
        if doc_number_pdf == self.propertyutil.get_property("document_pdf_no"):
            return True
        return False
    def assert_doc_recent_library(self):
        if self.propertyutil.get_property("doc_id") in self.recent_library:
            return False
        return True

    def click_content_aem_firstlev(self):
        self.seleniumutil.wait_for_element_visible(self.doc_first_level)
        self.seleniumutil.click(*self.doc_first_level)
        print("CLicked on content from library")

    def click_content_aem_secondlev(self):
        self.seleniumutil.wait_for_element_visible(self.doc_second_level)
        self.seleniumutil.click(*self.doc_second_level)
        print("CLicked on content from library")

    def click_content_aem_thirdlev(self):
        self.seleniumutil.wait_for_element_visible(self.doc_third_level)
        self.seleniumutil.click(*self.doc_third_level)
        print("CLicked on content from library")

    def click_content_aem_fourthlev(self):
        self.seleniumutil.wait_for_element_visible(self.doc_fourth_level)
        self.seleniumutil.click(*self.doc_fourth_level)
        print("CLicked on content from library")
