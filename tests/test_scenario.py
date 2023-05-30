from pages.login_page import LoginPage
from pages.veeva_document_verify import VeevatoAem
from pages.veeva_to_aem_transfer import VeevatoAemContentTransfer
from pages.xpconnect_to_veeva import AemToVeeva
from utils.property_util import PropertyUtils
from utils.webdriverutil import WebDriverUtil

propertyutil = PropertyUtils()


def test_scenario1(set_up):
    aem_to_veeva = AemToVeeva(WebDriverUtil.getwebdriverinstance())
    veevatoaem = VeevatoAem(WebDriverUtil.getwebdriverinstance())

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
    aem_to_veeva.new_tab(propertyutil.get_property("veeva_url"))
    aem_to_veeva.switch_window("Veeva")
    loginpage = LoginPage(WebDriverUtil.getwebdriverinstance())
    loginpage.enter_veeva_username(propertyutil.get_property("veeva_username"))
    loginpage.click_continue_veeva_login()
    loginpage.enter_veeva_password(propertyutil.get_property("veeva_password"))
    loginpage.click_veeva_login()
    veevatoaem.click_all_library()
    veevatoaem.click_content_aem()
    veevatoaem.assert_document_number()


def test_scenario2():
    print("____________Scenario 2________________")
    veevatoaem = VeevatoAem(WebDriverUtil.getwebdriverinstance())
    veevaaemdoctransfer = VeevatoAemContentTransfer(WebDriverUtil.getwebdriverinstance())
    loginpage = LoginPage(WebDriverUtil.getwebdriverinstance())
    loginpage.browse_url_app(propertyutil.get_property("veeva_url"))
    loginpage.enter_veeva_username(propertyutil.get_property("veeva_username"))
    loginpage.click_continue_veeva_login()
    loginpage.enter_veeva_password(propertyutil.get_property("veeva_password"))
    loginpage.click_veeva_login()
    veevatoaem.click_all_library()
    veevaaemdoctransfer.document_types_veeva()
    veevaaemdoctransfer.component_asset_veeva()
    veevaaemdoctransfer.content_component_asset_veeva()
    veevaaemdoctransfer.menu_for_aem_env_veeva()
    veevaaemdoctransfer.demo2_env_aem()
    veevaaemdoctransfer.close_page_icon()
    veevaaemdoctransfer.global_document_id()
