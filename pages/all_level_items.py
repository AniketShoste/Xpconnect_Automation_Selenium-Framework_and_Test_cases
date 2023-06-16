import time

from selenium.webdriver.common.by import By

from pages.base import BaseSetup


class All_level_content(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)
        print("login page init")
        # self.driver = driver
        # self.selenium_utility = SeleniumUtility(self.driver)


    #arrows
    we_retail_arrow= (By.CSS_SELECTOR, "[data-foundation-collection-item-id='\/content\/we-retail'] .foundation-layout-util-subtletext")
    language_master_arrow = (By.CSS_SELECTOR,"coral-columnview-column:nth-of-type(2) > coral-columnview-column-content[role='presentation'] > coral-columnview-item:nth-of-type(1)")
    english_arrow = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='\/content\/we-retail\/language-masters\/en'] coral-columnview-item-content")
    experience_arrow = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='\/content\/we-retail\/language-masters\/en\/experience'] coral-columnview-item-content")

    #icons
    language_master_icon = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='\/content\/we-retail\/language-masters'] coral-columnview-item-thumbnail")
    english_icon = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='\/content\/we-retail\/language-masters\/en'] coral-columnview-item-thumbnail")
    experience_icon = (By.CSS_SELECTOR, "[data-foundation-collection-item-id='\/content\/we-retail\/language-masters\/en\/experience'] coral-columnview-item-thumbnail")
    arctic_surf = (By.CSS_SELECTOR,"[data-foundation-collection-item-id='\/content\/we-retail\/language-masters\/en\/experience\/arctic-surfing-in-lofoten'] coral-columnview-item-thumbnail")




    def click_we_ret_arrow(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.we_retail_arrow)
        self.seleniumutil.click(*self.we_retail_arrow)

    def click_language_master_arrow(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.language_master_arrow)
        self.seleniumutil.click(*self.language_master_arrow)

    def click_language_master_icon(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.language_master_icon)
        self.seleniumutil.click(*self.language_master_icon)

    def click_english(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.english_arrow)
        self.seleniumutil.click(*self.english_arrow)

    def click_english_icon(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.english_icon)
        self.seleniumutil.click(*self.english_icon)

    def click_experience(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.experience_arrow)
        self.seleniumutil.click(*self.experience_arrow)

    def click_experience_icon(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.experience_icon)
        self.seleniumutil.click(*self.experience_icon)

    def click_arctic_surf(self):
        time.sleep(2)
        self.seleniumutil.wait_for_element_clickable(self.arctic_surf)
        self.seleniumutil.click(*self.arctic_surf)

