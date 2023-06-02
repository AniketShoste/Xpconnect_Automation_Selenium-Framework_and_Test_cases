import time

from pages.base import BaseSetup
from pages.login_page import LoginPage
from pages.validate_veeva_doc_aem import ValidateVeevaDocAem
from pages.veeva_document_verify import VeevatoAem
from pages.veeva_to_aem_transfer import VeevatoAemContentTransfer
from pages.xpconnect_to_veeva import AemToVeeva
from utils.property_util import PropertyUtils
from utils.webdriverutil import WebDriverUtil

propertyutil = PropertyUtils()


def test_scenario1(set_up):
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



def test_scenario2(set_up):
    print("____________Scenario 2________________")
    veevatoaem = VeevatoAem(WebDriverUtil.getwebdriverinstance())
    veevaaemdoctransfer = VeevatoAemContentTransfer(WebDriverUtil.getwebdriverinstance())
    loginpage = LoginPage(WebDriverUtil.getwebdriverinstance())
    validateveevatoaem = ValidateVeevaDocAem(WebDriverUtil.getwebdriverinstance())
    base_page = BaseSetup(WebDriverUtil.getwebdriverinstance())
    time.sleep(3)
    veevatoaem.click_all_library()
    veevaaemdoctransfer.document_types_veeva()
    veevaaemdoctransfer.component_asset_veeva()
    base_page.refresh_page()
    veevaaemdoctransfer.content_component_asset_veeva()
    veevaaemdoctransfer.menu_for_aem_env_veeva()
    veevaaemdoctransfer.demo2_env_aem()
    veevaaemdoctransfer.close_page_icon()
    veevaaemdoctransfer.global_document_id()
    time.sleep(3)
    base_page.switch_window("AEM")
    validateveevatoaem.click_home_page_aem()
    print("--------Clicked on Adobe Experience Manager------")
    validateveevatoaem.click_folder_asset()
    validateveevatoaem.click_folder_files()
    validateveevatoaem.click_folder_xpconnect()
    validateveevatoaem.click_folder_demovault()
    validateveevatoaem.click_content_component_asset()
    validateveevatoaem.click_xpconnect_menu()
    validateveevatoaem.click_v_metadata()
    validateveevatoaem.click_doc_id_vm()
