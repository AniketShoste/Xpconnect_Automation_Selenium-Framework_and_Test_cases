import threading

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

'''
this class initialize the web driver and handles the browser dependency

'''


class WebDriverUtil:
    __d_instance = None
    driver = None
    __lock = threading.Lock()

    @classmethod
    def get_instance(cls):
        if not cls.__d_instance:
            with cls.__lock:
                if not cls.__d_instance:
                    cls.__d_instance = cls()
        return cls.__d_instance

    # def getwebdriver(self, browser):
    #     global driver
    #     match browser:
    #         case "Chrome":
    #             driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #         case "Firefox":
    #             driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    #         case _:
    #             driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #
    #     driver.maximize_window()
    #     return driver

    def getwebdriver(self, browser):

        global driver
        if browser == "Chrome":
            options = webdriver.ChromeOptions()
            options.headless = True
            options.add_argument("--window-size=1920,1080")
            capabilities = webdriver.DesiredCapabilities().CHROME.copy()
            capabilities['acceptInsecureCerts'] = True
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options,
                                      desired_capabilities=capabilities)
        elif browser == "Firefox":
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        else:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.maximize_window()
        return driver

    @staticmethod
    def getwebdriverinstance():
        if driver:
            return driver
