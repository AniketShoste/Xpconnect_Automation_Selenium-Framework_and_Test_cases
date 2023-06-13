import random
import time
from datetime import datetime

from selenium.webdriver.common.by import By

from pages.base import BaseSetup

'''
This class is transferring content from veeva to aem
'''


class Module_Content_Builder(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)

    '''
          Locators and methods of the page written on same page - This is part of page object model
    '''
    preview = (By.CSS_SELECTOR,"[data-layer='Preview'] coral-button-label")
    frame_mcb = (By.CSS_SELECTOR, "iframe#ContentFrame")
    modular_content_b = (By.CSS_SELECTOR,".navbar-nav.mr-auto > .nav-item:nth-child(1) .nav-link")
    search_box = (By.CSS_SELECTOR,"input#search-input")
    search_button = (By.CSS_SELECTOR,".btn.btn-primary.btn-search")
    veeva_module_selector = (By.CSS_SELECTOR,"div#list-tab > a")
    one_asset_claim = (By.CSS_SELECTOR,"div:nth-of-type(4) > .accordion-header > .accordion-button.collapsed > b")
    displayed_asset = (By.CSS_SELECTOR,"div#by > .column.first")
    displayed_asset_dropdown = (By.CSS_SELECTOR,"button#dropdownMenuLink-")
    select_displayed_asset = (By.CSS_SELECTOR,".dropdown-menu.show  .dropdown-item")
    associated_claim = (By.CSS_SELECTOR,".accordion-collapse.collapse.show  .list-group > a:nth-of-type(2) > .binding-type > .column.first")
    claims_associated_dropdown = (By.CSS_SELECTOR,"div:nth-of-type(1) > .card > .card-header.target > .add-claim.btn-group > .btn.btn-light.btn-sm.dropdown-toggle")
    select_associated_claim =(By.CSS_SELECTOR,".dropdown-menu.show  .dropdown-item")
    create_mcb=(By.CSS_SELECTOR,".accordion-collapse.collapse.show  .template-controls  .align-self-end.gap-2.inset.justify-content-center.row  .btn.btn-primary")
    enter_title = (By.CSS_SELECTOR,".modal-body .container > .row.inset:nth-child(2) .col > .column:nth-child(2) .form-control")
    create_mcb_button = (By.CSS_SELECTOR,".btn.btn-primary.submit")
    validate_content_link = (By.CSS_SELECTOR,"div.message a")
    def click_preview(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_visible(self.preview)
        self.seleniumutil.click(*self.preview)
        print("Click on preview ")

    def switch_to_appsetting_frame_mcb(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_visible(self.frame_mcb)
        self.seleniumutil.switch_to_frame(*self.frame_mcb)
        print("Switched frame")

    def click_modular_content_builder(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_visible(self.modular_content_b)
        self.seleniumutil.click_using_js(*self.modular_content_b)
        print("Click on modular content builder")

    def enter_value_search_box(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_visible(self.search_box)
        self.seleniumutil.input_text_using_js(self.propertyutil.get_property("veevamoduleselector"),*self.search_box)

        print("Enter Veeva Module Selector value")

    def click_search_box(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.search_button)
        self.seleniumutil.click_using_js(*self.search_button)
        print("Click on search button")

    def click_veeva_module_selector(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.veeva_module_selector)
        self.seleniumutil.click_using_js(*self.veeva_module_selector)
        print("Click on veeva module selector")

    def click_one_asset_claim(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.one_asset_claim)
        self.seleniumutil.click_using_js(*self.one_asset_claim)
        print("Click on one asset claim")

    def click_displayed_asset(self):
        time.sleep(2)
        #self.seleniumutil.wait_for_element_visible(self.displayed_asset)
        self.seleniumutil.click_using_js(*self.displayed_asset)
        print("Click on displayed asset option")

    def click_displayed_asset_dropdown(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.displayed_asset_dropdown)
        self.seleniumutil.click_using_js(*self.displayed_asset_dropdown)
        print("Click on displayed asset dropdown")

    def click_select_displayed_asset(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.select_displayed_asset)
        self.seleniumutil.click_using_js(*self.select_displayed_asset)
        print("select displayed asset")

    def click_associated_claim(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.associated_claim)
        self.seleniumutil.click_using_js(*self.associated_claim)
        print("click on associated claim")

    def click_claims_associated_dropdown(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.claims_associated_dropdown)
        self.seleniumutil.click_using_js(*self.claims_associated_dropdown)
        print("click on associated claim dropdown")

    def click_select_associated_claim(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.select_associated_claim)
        self.seleniumutil.click_using_js(*self.select_associated_claim)
        print("click on select associated claim")
    def click_create_mcb(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.create_mcb)
        self.seleniumutil.click_using_js(*self.create_mcb)
        print("click on create content")

    def enter_title_content(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_visible(self.enter_title)
        title = self.propertyutil.get_property("titlemodularcontent")+str(random.randint(1,10001))
        self.seleniumutil.input_text_using_js(title, *self.enter_title)
        self.propertyutil.set_property("settitle",title)
        print("Enter content title")

    def click_create_mcb_button(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.create_mcb_button)
        self.seleniumutil.click_using_js(*self.create_mcb_button)
        print("submit create content")

    def check_validate_content_link(self):
        time.sleep(2)
        print("Content created",self.seleniumutil.verify_text_using_js(*self.validate_content_link))
        print("title of the content",self.propertyutil.get_property("settitle"))
        if self.propertyutil.get_property("settitle") in self.seleniumutil.verify_text_using_js(*self.validate_content_link):
            return True
        return False
