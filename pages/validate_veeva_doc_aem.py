from pages.base import BaseSetup
from selenium.webdriver.common.by import By


class ValidateVeevaDocAem(BaseSetup):
    def __init__(self, driver):
        super().__init__(driver)


    home_page_aem = (By.CSS_SELECTOR, "#globalNavHeader [icon]")
    component_asset = (By.CSS_SELECTOR, "li:nth-of-type(3) > .categoryTerm.doc_link.vv-facet-term")
    content_component_asset = (By.CSS_SELECTOR, "div[name='book'] .mimeTypeBox > .docThumbnail > .doc_preview_thumbnail.img_float_left")
    menu_for_aem_env = (By.CSS_SELECTOR,".css-14vl23m-childrenCSS-css-css  .css-11eaezd-buttonCSS-buttonCSS-buttonCSS-buttonCSS-buttonCSS-buttonCSS-DropdownMenu-DropdownMenu > .css-1il8e9o-DropdownMenu")
    demo_env = (By.CSS_SELECTOR, "[data-value='dynamicAction\:LifecycleUserAction10']")
    close_page = (By.CSS_SELECTOR, ".closeIFrameTemplate")
    global_doc_id = (By.CSS_SELECTOR, ".docInfoValue-docGlobalId_b")