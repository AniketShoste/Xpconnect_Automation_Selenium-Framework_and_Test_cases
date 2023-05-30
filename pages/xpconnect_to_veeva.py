import time

from pages.base import BaseSetup
from selenium.webdriver.common.by import By


class AemToVeeva(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)
        print("login page init")
        # self.driver = driver
        # self.selenium_utility = SeleniumUtility(self.driver)

    we_retail = (By.XPATH,"//coral-columnview-item-thumbnail//img[@src='/content/we-retail.thumb.48.48.png?ck=1602193946']")
    xp_connect =(By.XPATH, "//a[@id='xpconnect-trigger']")
    send_to_veeva = (By.XPATH, "//button[@title='XpConnect® - Send to Veeva Vault']")
    select_workflow =(By.XPATH,"//coral-dialog[@role='dialog']//coral-dialog-content[@class='coral3-Dialog-content']/coral-select[@name='model']/button[@type='button']")
    xp_connect_workflow =(By.CSS_SELECTOR,".coral3-Dialog-content  coral-overlay[role='presentation'] > coral-selectlist[role='listbox'] > coral-selectlist-item:nth-of-type(2)")
    start_workflow = (By.CSS_SELECTOR,".coral3-Button.coral3-Button--primary.xpConnect-cq-WorkflowStart-submit > coral-button-label")
    warning_pop_up_checkbox = (By.CSS_SELECTOR, ".coral3-Checkbox > .coral3-Checkbox-input")
    proceed_workflow = (By.CSS_SELECTOR,"coral-dialog#workflowLargeAssetsWarning  .coral3-Dialog-footer > button:nth-of-type(2) > coral-button-label")
    veeva_metadata = (By.CSS_SELECTOR, "div#pageinfo-data > button[title='Veeva Metadata']")
    document_number_aem = (By.CSS_SELECTOR, "tr:nth-of-type(3) > td:nth-of-type(2)")

    def click_html_page(self):
        print(*self.we_retail)
        self.seleniumutil.wait_for_element(self.we_retail)
        self.seleniumutil.click(*self.we_retail)
        print("We retail clicked")

    def click_on_xpconnect(self):
        self.seleniumutil.wait_for_element(self.xp_connect)
        self.seleniumutil.click(*self.xp_connect)
        print("Clcked on Xpconnect")
        #time.sleep(5)

    def click_send_to_veeva(self):
        self.seleniumutil.wait_for_element(self.send_to_veeva)
        self.seleniumutil.click(*self.send_to_veeva)
        print("Clcked on send to veeva")
        #time.sleep(10)

    def click_select_workflow(self):
        self.seleniumutil.wait_for_element(self.select_workflow)
        self.seleniumutil.click(*self.select_workflow)
        print("Click on select workflow")
        #time.sleep(10)

    def click_xpconnect_workflow(self):
        self.seleniumutil.wait_for_element(self.xp_connect_workflow)
        self.seleniumutil.click(*self.xp_connect_workflow)
        print("Click on xpconnect workflow")
        #time.sleep(10)

    def click_start_workflow(self):
        self.seleniumutil.wait_for_element(self.start_workflow)
        self.seleniumutil.click(*self.start_workflow)
        print("Click on start workflow")
        #time.sleep(10)

    def click_warning_pop_up_checkbox(self):
        self.seleniumutil.wait_for_element(self.warning_pop_up_checkbox)
        self.seleniumutil.click(*self.warning_pop_up_checkbox)
        print("Click on warning pop up checkbox")
        #time.sleep(10)

    def click_proceed_workflow(self):
        self.seleniumutil.wait_for_element(self.proceed_workflow)
        self.seleniumutil.click(*self.proceed_workflow)
        print("Click on proceed workflow")
        time.sleep(15)

    def click_veeva_metadata(self):
        self.seleniumutil.wait_for_element(self.veeva_metadata)
        self.seleniumutil.click(*self.veeva_metadata)
        print("Click on proceed workflow")
        #time.sleep(10)

    def get_document_id(self):
        self.seleniumutil.wait_for_element(self.document_number_aem)
        doc_id = self.seleniumutil.text(*self.document_number_aem)
        self.propertyutil.set_property("doc_id",doc_id)
        print("Document number is", doc_id)
        #time.sleep(10)

    def new_tab(self,url):
        self.seleniumutil.open_new_tab(url)
        print("new tab opened")
        time.sleep(5)

    def switch_window(self,windowtitle):
        self.seleniumutil.switch_to_window(windowtitle)
        print("Switch to window")
        time.sleep(5)

    def refresh_page(self):
        self.seleniumutil.refresh()