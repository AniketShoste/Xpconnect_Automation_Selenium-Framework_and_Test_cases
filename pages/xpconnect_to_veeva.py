import time

from selenium.webdriver.common.by import By

from pages.base import BaseSetup

'''
This class is sending document from AEM to Veeva using xpconnect workflow
'''
class AemToVeeva(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)
        print("login page init")



    '''
          Locators and methods of the page written on same page - This is part of page object model
    '''

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
    No_metadata_to_display_popup = (By.CSS_SELECTOR,"coral-dialog[role='dialog'] button[title='Close'] > coral-icon[role='img']")
    we_retail_navigate = (By.CSS_SELECTOR,"coral-columnview-column[role='presentation'] > coral-columnview-column-content[role='presentation'] > coral-columnview-item:nth-of-type(6)")
    spain =  (By.CSS_SELECTOR,"[data-foundation-collection-item-id='\/content\/we-retail\/es'] [itemprop='title']")

    espanol = (By.CSS_SELECTOR,
               "[data-foundation-collection-item-id='\/content\/we-retail\/es\/es'] coral-columnview-item-thumbnail")
    xp_connect_mp4_workflow = (
    By.CSS_SELECTOR, "coral-selectlist[role='listbox'] > coral-selectlist-item:nth-of-type(4)")
    escape = (By.CSS_SELECTOR, "coral-actionbar-secondary[role='toolbar'] > .coral3-ActionBar-item  coral-icon")
    notification = (By.CSS_SELECTOR,
                    "coral-shell-menubar-item:nth-of-type(4) > .coral3-Button.coral3-Button--minimal.coral3-Shell-menu-button")
    content_type = (By.CSS_SELECTOR, "div:nth-of-type(1) > .granite-shell-badge-item-link")
    failure_message_mp4 = (By.CSS_SELECTOR, "input[name='failureMessage']")
    document_pdf_no_i = (By.CSS_SELECTOR,"tr:nth-of-type(3) > td:nth-of-type(2)")

    germany = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='\/content\/we-retail\/de'] [itemprop='title']")
    deutsh = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='\/content\/we-retail\/de\/de'] coral-columnview-item-thumbnail")
    xp_connect_pdf_image_workflow = (By.CSS_SELECTOR,".coral3-Dialog-content  coral-overlay[role='presentation'] > coral-selectlist[role='listbox'] > coral-selectlist-item:nth-of-type(3)")
    failure_message = (By.NAME, "failureMessage")



    def click_html_page(self):
        print(*self.we_retail)
        self.seleniumutil.wait_for_element_visible(self.we_retail)
        self.seleniumutil.click(*self.we_retail)
        print("We retail clicked")

    def click_on_xpconnect(self):
        self.seleniumutil.wait_for_element_visible(self.xp_connect)
        self.seleniumutil.click(*self.xp_connect)
        print("Clcked on Xpconnect")

    def click_send_to_veeva(self):
        self.seleniumutil.wait_for_element_visible(self.send_to_veeva)
        self.seleniumutil.click(*self.send_to_veeva)
        print("Clcked on send to veeva")

    def click_select_workflow(self):
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

    def click_veeva_metadata(self):
        self.seleniumutil.wait_for_element_visible(self.veeva_metadata)
        self.seleniumutil.click(*self.veeva_metadata)
        print("Click on proceed workflow")

    def get_document_id(self):
        self.seleniumutil.wait_for_element_visible(self.document_number_aem)
        doc_id = self.seleniumutil.text(*self.document_number_aem)
        self.propertyutil.set_property("doc_id",doc_id)
        print("Document number is", doc_id)

    def click_close_metadata_popup(self):
        self.seleniumutil.wait_for_element_visible(self.No_metadata_to_display_popup)
        self.seleniumutil.click(*self.No_metadata_to_display_popup)
        print("Close the no metadata to display popup")

    def click_we_retail_navigate(self):
        self.seleniumutil.wait_for_element_visible(self.we_retail_navigate)
        self.seleniumutil.click(*self.we_retail_navigate)
        print("We Retail clicked")



    def click_spain(self):
        self.seleniumutil.wait_for_element_visible(self.spain)
        self.seleniumutil.click(*self.spain)
        print("Spain clicked")

    def click_espanol(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element_visible(self.espanol)
        self.seleniumutil.click(*self.espanol)
        print("Espanol clicked")

    def click_Xpconnect_mp4(self):
        self.seleniumutil.wait_for_element_visible(self.xp_connect_mp4_workflow)
        self.seleniumutil.click(*self.xp_connect_mp4_workflow)
        print("Click on Xp_connect_PNG/MP4_workflow ")
    def click_to_close_navigation_bar(self):
        self.seleniumutil.wait_for_element_clickable(self.escape)
        self.seleniumutil.click(*self.escape)
        print("Click to escape")

    def click_notification(self):
        time.sleep(4)
        self.seleniumutil.wait_for_element_clickable(self.notification)
        self.seleniumutil.click(*self.notification)
        print("Click on Notification")

    def click_notification_content_type(self):
        time.sleep(4)
        self.seleniumutil.wait_for_element_visible(self.content_type)
        self.seleniumutil.click(*self.content_type)
        print("Click on : Determine Content Type")

    def get_failure_message_mp4(self):
        self.seleniumutil.wait_for_element_visible(self.failure_message_mp4)
        fail_txt = self.seleniumutil.get_attribute_by_value(*self.failure_message_mp4)
        self.propertyutil.set_property("fail_txt",fail_txt)
        print("Failure Message is : ",fail_txt)

    def assert_mp4_not_sent(self):
        failure = "No route found to continue from step node1 in model /var/workflow/models/amsys---xpconnect-png-mp4-workflow. Probably a configuration error."
        if failure == self.propertyutil.get_property("fail_txt"):
            return True
        return False

    def take_document_number_pdf(self):
        self.seleniumutil.wait_for_element_visible(self.document_pdf_no_i)
        document_pdf_no = self.seleniumutil.text(*self.document_pdf_no_i)
        self.propertyutil.set_property("document_pdf_no", document_pdf_no)
        print("Document number pdf no is", document_pdf_no)

    def click_Germany(self):
        self.seleniumutil.wait_for_element_visible(self.germany)
        self.seleniumutil.click(*self.germany)
        print("Germany clicked")

    def click_Deutsh(self):
        time.sleep(3)
        self.seleniumutil.wait_for_element_visible(self.deutsh)
        self.seleniumutil.click(*self.deutsh)
        print("Deutsh clicked")

    def click_Xpconnect_pdf_image(self):
        self.seleniumutil.wait_for_element_visible(self.xp_connect_pdf_image_workflow)
        self.seleniumutil.click(*self.xp_connect_pdf_image_workflow)
        print("Click on Xp_connect_pdf_image_workflow ")

    def get_failure_message(self):
        self.seleniumutil.wait_for_element_visible(self.failure_message)
        fail_msg_txt = self.seleniumutil.get_attribute_by_value(*self.failure_message)
        self.propertyutil.set_property("fail_msg_txt", fail_msg_txt)
        print("Failure Message is : ", fail_msg_txt)

    def assert_html_doc_not_sent(self):
        failure_txt = "No route found to continue from step node1 in model /var/workflow/models/amsys---xpconnect-pdf-image-workflow. Probably a configuration error."
        if failure_txt == self.propertyutil.get_property("fail_msg_txt"):
            return True
        return False