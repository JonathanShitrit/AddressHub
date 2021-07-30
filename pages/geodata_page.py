from pages.base_page import BasePage
from utils.locators import GeoDataLocators
from selenium.webdriver.support.ui import Select
from utils.env_loader import *
import time

class GeoDataPage(BasePage):
    def __init__(self, driver):
        self.locator = GeoDataLocators
        super(GeoDataPage, self).__init__(driver, "https://www.geodataplus.com/")  # Python2 version
        self.new_tab()

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGIN_MODAL) else False

    def open_login_modal(self):
        self.find_element(*self.locator.LOGIN_MODAL).click()
        # element = self.find_element(*self.locator.LOGIN_MODAL) 
        # self.driver.execute_script("arguments[0].setAttribute('class','modal fade ModalsVik inputModal LoginModal main-login in')")
        # self.driver.execute_script("arguments[0].setAttribute('style','display: block; padding-right: 16px;')")

        
    def open_login_mobile_modal(self):
        self.find_element(*self.locator.LOGIN_MODAL_MOBILE).click()

    def enter_email(self):
        self.find_element(*self.locator.LOGIN_EMAIL_INPUT).send_keys(EMAIL)    

    def enter_password(self):
        self.find_element(*self.locator.LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)    

    def click_login_btn(self):
        self.find_element(*self.locator.LOGIN_SUBMIT_BTN).click()

    def enter_street_number(self):
        self.hover(*self.locator.HOUSE_NUMBER_INPUT)
        self.find_element(*self.locator.HOUSE_NUMBER_INPUT).send_keys(STREET_NUMBER)
    
    def enter_street_name(self):
        self.find_element(*self.locator.STREET_NAME_INPUT).send_keys(STREET_NAME + " ")

    def enter_street_suffix(self):
        self.find_element(*self.locator.STREET_NAME_INPUT).send_keys(SUFFIX)

    def select_from_dropdown(self):
        Select(self.find_element(*self.locator.BORO_DROPDOWN)).select_by_value(get_boro_id())

    def click_go_btn(self):
        self.find_element(*self.locator.GO_BTN).click()


    def login(self):
        self.open_login_modal()
        self.enter_email()
        self.enter_password()
        self.click_login_btn()

    # def insert_property_address(self):
    #     self.enter_street_number()
    #     self.enter_street_name()
    #     self.enter_street_suffix()
    #     self.select_from_dropdown()

    def run_full_test(self):
        print("Logging into geodata...")
        self.login()
