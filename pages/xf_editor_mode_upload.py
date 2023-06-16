import time

from selenium.webdriver.common.by import By

from pages.base import BaseSetup

'''
This class is sending document from AEM to Veeva using xpconnect workflow
'''


class xf_editor(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)
        print("login page init")

    '''
          Locators and methods of the page written on same page - This is part of page object model
    '''

    xp_connect_editor = (By.XPATH, r"/html//a[@id='xpconnect-trigger']")
    send_to_veeva = (By.CSS_SELECTOR, "button[title='XpConnect® - Send to Veeva Vault']")
    select_workflow = (By.XPATH,
                       "//body/coral-dialog[2]//coral-dialog-content[@class='coral3-Dialog-content']/coral-select[@name='model']/button[@type='button']")
    xp_connect_workflow = (By.CSS_SELECTOR,
                           "coral-dialog:nth-of-type(2) .coral3-Dialog-content  coral-overlay[role='presentation'] > coral-selectlist[role='listbox'] > coral-selectlist-item:nth-of-type(2)")
    start_workflow = (
    By.CSS_SELECTOR, ".coral3-Dialog-footer > .coral3-Button.coral3-Button--primary.xpConnect-cq-WorkflowStart-submit")
    warning_pop_up_checkbox = (By.CSS_SELECTOR, ".coral3-Checkbox > .coral3-Checkbox-input")
    proceed_workflow = (By.CSS_SELECTOR,
                        "coral-dialog#workflowLargeAssetsWarning  .coral3-Dialog-footer > button:nth-of-type(2) > coral-button-label")
    veeva_metadata_editor = (By.CSS_SELECTOR, "button[title='Veeva Metadata']")
    document_number_aem = (By.CSS_SELECTOR, "tr:nth-of-type(3) > td:nth-of-type(2)")
    wknd_events = (
    By.CSS_SELECTOR, r"[data-foundation-collection-item-id='\/content\/wknd-events'] coral-columnview-item-thumbnail")
    edit = (By.CSS_SELECTOR,
            r"[data-foundation-collection-action='\{\"target\"\:\"\.cq-siteadmin-admin-childpages\"\,\"activeSelectionCount\"\:\"multiple\"\,\"action\"\:\"cq\.wcm\.open\"\,\"data\"\:\{\"cookiePath\"\:\"\/\"\,\"href\"\:\"\/bin\/wcmcommand\?cmd\=open\&_charset_\=utf-8\&path\=\{item\}\"\}\}']")
    editor = (By.CSS_SELECTOR, r"coral-actionbar-secondary [data-layer='Edit']")
    edit_xf = (By.CSS_SELECTOR, "coral-actionbar-item:nth-of-type(2)  coral-button-label > .granite-command-inline")
    main_menu = (By.CSS_SELECTOR, "a#globalNavHeader > coral-shell-homeanchor-label")
    experience_fragments = (By.CSS_SELECTOR, "coral-masonry-item:nth-of-type(3) > div[role='link']")
    xf_drilldown = (
    By.CSS_SELECTOR, "coral-columnview-column-content[role='presentation'] > coral-columnview-item:nth-of-type(1)")
    xf_drill1 = (
    By.CSS_SELECTOR, "coral-columnview-column-content[role='presentation'] > coral-columnview-item:nth-of-type(3)")
    xf_to_send = (By.CSS_SELECTOR,
                  r"[data-foundation-collection-item-id='\/content\/experience-fragments\/XpConnect\/test1\/master'] coral-columnview-item-thumbnail")

    def click_send_to_veeva_editor(self):
        self.seleniumutil.wait_for_element_visible(self.send_to_veeva)
        self.seleniumutil.click(*self.send_to_veeva)
        print("Clcked on send to veeva")

    def click_select_workflow_editor(self):
        self.seleniumutil.wait_for_element_visible(self.select_workflow)
        self.seleniumutil.click(*self.select_workflow)
        print("Click on select workflow")

    def click_xpconnect_workflow(self):
        self.seleniumutil.wait_for_element_visible(self.xp_connect_workflow)
        self.seleniumutil.click(*self.xp_connect_workflow)
        print("Click on xpconnect workflow")

    def click_start_workflow(self):
        self.seleniumutil.wait_for_element_visible(self.start_workflow)
        self.seleniumutil.click(*self.start_workflow)
        print("Click on start workflow")

    def click_warning_pop_up_checkbox(self):
        self.seleniumutil.wait_for_element_visible(self.warning_pop_up_checkbox)
        self.seleniumutil.click(*self.warning_pop_up_checkbox)
        print("Click on warning pop up checkbox")

    def click_proceed_workflow(self):
        self.seleniumutil.wait_for_element_visible(self.proceed_workflow)
        self.seleniumutil.click(*self.proceed_workflow)
        print("Click on proceed workflow")

    def click_veeva_metadata_editor(self):
        self.seleniumutil.wait_for_element_visible(self.veeva_metadata_editor)
        self.seleniumutil.click(*self.veeva_metadata_editor)
        print("Click on proceed workflow")

    def get_document_id(self):
        self.seleniumutil.wait_for_element_visible(self.document_number_aem)
        doc_id = self.seleniumutil.text(*self.document_number_aem)
        self.propertyutil.set_property("doc_id", doc_id)
        print("Document number is", doc_id)

    def click_wknd_events(self):
        # print(*self.we_retail)
        self.seleniumutil.wait_for_element_visible(self.wknd_events)
        self.seleniumutil.click(*self.wknd_events)
        print("WKND Events clicked")

    def click_edit(self):
        # print(*self.we_retail)
        self.seleniumutil.wait_for_element_visible(self.edit)
        self.seleniumutil.click(*self.edit)
        print("Edit clicked")

    def click_edit_xf(self):
        # print(*self.we_retail)
        self.seleniumutil.wait_for_element_visible(self.edit_xf)
        self.seleniumutil.click(*self.edit_xf)
        print("Edit clicked")

    def click_editor(self):
        # print(*self.we_retail)
        self.seleniumutil.wait_for_element_visible(self.editor)
        self.seleniumutil.click(*self.editor)
        print("Editor Mode Selected")

    def click_xp_connect_editor(self):
        # print(*self.we_retail)
        self.seleniumutil.wait_for_element_visible(self.xp_connect_editor)
        self.seleniumutil.click(*self.xp_connect_editor)
        print("XpConnect Plugin Clicked")

    def click_main_menu(self):
        # print(*self.we_retail)
        self.seleniumutil.wait_for_element_visible(self.main_menu)
        self.seleniumutil.click(*self.main_menu)
        print("Main Menu clicked")

    def click_experience_fragments(self):
        # print(*self.we_retail)
        self.seleniumutil.wait_for_element_visible(self.experience_fragments)
        self.seleniumutil.click(*self.experience_fragments)
        print("Experience Fragments clicked")

    def click_xf_drilldown(self):
        # print(*self.we_retail)
        self.seleniumutil.wait_for_element_visible(self.xf_drilldown)
        self.seleniumutil.click(*self.xf_drilldown)
        print("XpConnect Fragments expanded")

    def click_xf_drilldown1(self):
        # print(*self.we_retail)
        self.seleniumutil.wait_for_element_visible(self.xf_drill1)
        self.seleniumutil.click(*self.xf_drill1)
        print("XpConnect Fragments expanded")

    def click_xf_to_send(self):
        # print(*self.we_retail)
        self.seleniumutil.wait_for_element_visible(self.xf_to_send)
        self.seleniumutil.click(*self.xf_to_send)
        print("XpConnect Fragment selected")
