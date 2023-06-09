import time

from pages.aem_appsetting import AEM_Appsetting
from pages.base import BaseSetup
from pages.login_page import LoginPage
from pages.validate_veeva_doc_aem import ValidateVeevaDocAem
from pages.veeva_document_verify import VeevatoAem
from pages.veeva_to_aem_transfer import VeevatoAemContentTransfer
from pages.xpconnect_to_veeva import AemToVeeva
from utils.property_util import PropertyUtils
from utils.webdriverutil import WebDriverUtil

propertyutil = PropertyUtils()
'''
Test cases gets executed from this file. 
'''

def test_aem_to_veeva(set_up):
    print("____________Scenario 1________________")
    aem_to_veeva = AemToVeeva(WebDriverUtil.getwebdriverinstance())
    veevatoaem = VeevatoAem(WebDriverUtil.getwebdriverinstance())
    base_page = BaseSetup(WebDriverUtil.getwebdriverinstance())
    base_page.switch_window("AEM")
    aem_to_veeva.click_html_page()
    aem_to_veeva.click_on_xpconnect()
    aem_to_veeva.click_send_to_veeva()
    aem_to_veeva.click_select_workflow()
    aem_to_veeva.click_xpconnect_workflow()
    aem_to_veeva.click_start_workflow()
    aem_to_veeva.click_warning_pop_up_checkbox()
    aem_to_veeva.click_proceed_workflow()
    aem_to_veeva.refresh_page()
    aem_to_veeva.click_html_page()
    aem_to_veeva.click_on_xpconnect()
    aem_to_veeva.click_veeva_metadata()
    aem_to_veeva.get_document_id()
    aem_to_veeva.switch_window("Veeva")
    veevatoaem.click_all_library()
    veevatoaem.click_content_aem()
    veevatoaem.assert_document_number()



def test_veeva_to_aem(set_up):
    print("____________Scenario 2________________")
    veevatoaem = VeevatoAem(WebDriverUtil.getwebdriverinstance())
    veevaaemdoctransfer = VeevatoAemContentTransfer(WebDriverUtil.getwebdriverinstance())
    validateveevatoaem = ValidateVeevaDocAem(WebDriverUtil.getwebdriverinstance())
    base_page = BaseSetup(WebDriverUtil.getwebdriverinstance())
    veevatoaem.click_all_library()
    veevaaemdoctransfer.document_types_veeva()
    veevaaemdoctransfer.component_asset_veeva()
    base_page.refresh_page()
    veevaaemdoctransfer.content_component_asset_veeva()
    veevaaemdoctransfer.menu_for_aem_env_veeva()
    veevaaemdoctransfer.demo2_env_aem()
    veevaaemdoctransfer.close_page_icon()
    veevaaemdoctransfer.global_document_id()
    base_page.switch_window("AEM")
    validateveevatoaem.click_home_page_aem()
    validateveevatoaem.click_folder_asset()
    validateveevatoaem.click_folder_files()
    validateveevatoaem.click_folder_xpconnect()
    validateveevatoaem.click_folder_demovault()
    validateveevatoaem.scroll_content_component_asset()
    validateveevatoaem.click_content_component_asset()
    validateveevatoaem.click_xpconnect_menu()
    validateveevatoaem.click_v_metadata()
    validateveevatoaem.assert_document_id_veeva_to_aem()

def test_aem_application_setting(set_up):
    print("____________Scenario 3________________")
    base_page = BaseSetup(WebDriverUtil.getwebdriverinstance())
    aemappsetting = AEM_Appsetting(WebDriverUtil.getwebdriverinstance())
    base_page.switch_window("AEM")
    aemappsetting.click_xpconnect_content()
    aemappsetting.click_app_setting()
    time.sleep(5)
    aemappsetting.click_xp_edit_button()
    time.sleep(5)
    base_page.switch_window("application-setting")
    aemappsetting.switch_to_appsetting_frame()
    time.sleep(5)
    aemappsetting.click_demo_dashboard()
    aemappsetting.click_veeva_credentials()
    aemappsetting.verify_veeva_url()
    aemappsetting.verify_veeva_username()
    aemappsetting.assert_veeva_url_username()


