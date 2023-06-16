import time

from selenium.webdriver.common.by import By

from pages.base import BaseSetup


class xpomni(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)
        print("login page init")
        super().__init__(driver)
        print("login page init")
        # self.driver = driver
        # self.selenium_utility = SeleniumUtility(self.driver)

    xp_omni_channel = (By.XPATH,"//div[@id='granite-shell-content']//coral-columnview[@role='tree']/coral-columnview-column[@role='presentation']/coral-columnview-column-content[@role='presentation']/coral-columnview-item[12]/coral-columnview-item-content/div[@title='XpOmniChannel']")
    xp_cap = (By.XPATH,"//div[@id='granite-shell-content']//coral-columnview[@role='tree']/coral-columnview-column[2]/coral-columnview-column-content[@role='presentation']/coral-columnview-item[2]/coral-columnview-item-content")
    email = (By.XPATH,"//div[@id='granite-shell-content']//coral-columnview[@role='tree']/coral-columnview-column[3]/coral-columnview-column-content[@role='presentation']/coral-columnview-item[2]/coral-columnview-item-content/div[@title='EMAIL']")
    IVA = (By.XPATH,"//div[@id='granite-shell-content']//coral-columnview[@role='tree']/coral-columnview-column[3]/coral-columnview-column-content[@role='presentation']/coral-columnview-item[1]/coral-columnview-item-content/div[@title='IVA']")
    web_page = (By.XPATH,"//div[@id='granite-shell-content']//coral-columnview[@role='tree']/coral-columnview-column[3]/coral-columnview-column-content[@role='presentation']/coral-columnview-item[3]/coral-columnview-item-content/div[@title='WebPage']")
    presentation_page = (By.XPATH,"//div[@id='granite-shell-content']//coral-columnview[@role='tree']/coral-columnview-column[4]/coral-columnview-column-content[@role='presentation']/coral-columnview-item[1]/coral-columnview-item-content/div[@title='Presentation Page']")
    home_page_content = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='/content/xpomnichannel/XpCap/IVA/presentation-page/slide-1'] coral-columnview-item-thumbnail")
    email_page = (By.XPATH,"//div[@id='granite-shell-content']//coral-columnview[@role='tree']/coral-columnview-column[4]/coral-columnview-column-content[@role='presentation']/coral-columnview-item[4]/coral-columnview-item-thumbnail")
    demo_web_site = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='/content/xpomnichannel/XpCap/WebPage/web-page'] coral-columnview-item-thumbnail")
    document_no = (By.XPATH,"//coral-dialog[@role='dialog']//coral-dialog-content[@class='coral3-Dialog-content']/table[@role='presentation']//table[@role='grid']/tbody/tr[3]/td[2]")
    home_document_no = (By.CSS_SELECTOR,"tr:nth-of-type(7) > td:nth-of-type(2)")
    email_content_doc_number = (By.CSS_SELECTOR,"tr:nth-of-type(3) > td:nth-of-type(2)")

    def click_omni_channel(self):
        self.seleniumutil.wait_for_element_clickable(self.xp_omni_channel)
        self.seleniumutil.click(*self.xp_omni_channel)
        print("XpOmni Channel clicked")

    def click_xp_cap(self):
        self.seleniumutil.wait_for_element_clickable(self.xp_cap)
        self.seleniumutil.click(*self.xp_cap)
        print("xpCap clicked")

    def click_iva(self):
        self.seleniumutil.wait_for_element_clickable(self.IVA)
        self.seleniumutil.click(*self.IVA)
        print("IVA clicked")

    def click_email(self):
        self.seleniumutil.wait_for_element_clickable(self.email)
        self.seleniumutil.click(*self.email)
        print("Email clicked")

    def click_web_page(self):
        self.seleniumutil.wait_for_element_clickable(self.web_page)
        self.seleniumutil.click(*self.web_page)
        print("WebPage clicked")


    def click_presentation_page(self):
        self.seleniumutil.wait_for_element_clickable(self.presentation_page)
        self.seleniumutil.click(*self.presentation_page)
        print("Presentation Page clicked")

    def click_home(self):
        self.seleniumutil.wait_for_element_clickable(self.home_page_content)
        self.seleniumutil.click(*self.home_page_content)
        print("Home clicked")


    def click_Email_page(self):
        self.seleniumutil.wait_for_element_clickable(self.email_page)
        self.seleniumutil.click(*self.email_page)
        print("Email Page clicked")


    def click_Demo_Web_site(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.demo_web_site)
        self.seleniumutil.click(*self.demo_web_site)
        print("Demo Web Site clicked")

    def get_demo_no(self):
        self.seleniumutil.wait_for_element_clickable(self.document_no)
        demo_no = self.seleniumutil.text(*self.document_no)
        self.propertyutil.set_property("demo_no", demo_no)
        print("Document Demo number  is", demo_no)

    def get_home_doc_no(self):
        self.seleniumutil.wait_for_element_clickable(self.home_document_no)
        home_no = self.seleniumutil.text(*self.home_document_no)
        self.propertyutil.set_property("home_no", home_no)
        print("Home Document number  is", home_no)

    def take_document_number_pdf(self):
        self.seleniumutil.wait_for_element_clickable(self.email_content_doc_number)
        email_content_id = self.seleniumutil.text(*self.email_content_doc_number)
        self.propertyutil.set_property("email_content_id", email_content_id)
        print("Document number pdf no is", email_content_id)
