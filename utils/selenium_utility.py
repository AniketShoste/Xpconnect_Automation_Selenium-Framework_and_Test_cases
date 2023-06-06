from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

'''
This is a utility class contains has all the selenium related methods which are common and all are reusable across framework.
'''
class SeleniumUtility():
    def __init__(self, driver):
        self.driver = driver
        print(self.driver)
        self.actions = ActionChains(self.driver)
    '''
    send keys method is used to input text in the textfield
    '''
    def send_keys(self, selector, locator, value):
        try:
            # self.driver.find_element(By.ID)
            self.driver.find_element(selector, locator).send_keys(value)
        except Exception as ex:
            print("Error while adding data", ex)

    def click(self, selector, locator):
        try:
            self.driver.find_element(selector, locator).click()
        except Exception as ex:
            print("Error while clicking on button", ex)

    def browse_url(self, url):
        try:
            print("browse url", self.driver)
            self.driver.get(url)

        except Exception as ex:
            print("Error while browsing an url", ex)

    def wait_for_element(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def open_new_tab(self, url):
        try:
            self.driver.execute_script(f"window.open('{url}');")
        except Exception as ex:
            print("While opening browser", ex)

    def switch_to_window(self, windowtitle):
        print("Window handles", self.driver.window_handles)
        print("current window handle",self.driver.current_window_handle)
        for each_window in self.driver.window_handles:
            print("current title",self.driver.title)
            if not (windowtitle.lower() in self.driver.title.lower()):
                self.driver.switch_to.window(each_window)
                print("each window",each_window)

    def text(self, selector, locator):
        try:
            return self.driver.find_element(selector, locator).text
        except Exception as ex:
            print("Error while clicking on button", ex)

    def refresh(self):
        self.driver.refresh()

    def close_browser(self):
        self.driver.quit()

    def click_js(self, locator):
        self.driver.execute_script(f"document.querySelector('${locator}').click();")

    def close_tab(self):
        self.driver.close()

    def take_screenshot(self):
        self.driver.save_screenshot("screenshot_store.png")
        print("screenshot captured")
