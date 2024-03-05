from pages.base_page import BasePage
from utils.locators import GeoDataLocators
from selenium.webdriver.support.ui import Select
from utils.env_loader import *
import time

class GeoDataPage(BasePage):
    def __init__(self, driver):
        self.locator = GeoDataLocators
        super().__init__(driver, "https://www.attomdata.com/solutions/property-navigator/signin") 
        self.new_tab()

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGIN_MODAL) else False

    def enter_email(self):
        self.find_element(*self.locator.LOGIN_EMAIL_INPUT).send_keys(EMAIL)    

    def enter_password(self):
        self.find_element(*self.locator.LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)    

    def click_login_btn(self):
        self.find_element(*self.locator.LOGIN_SUBMIT_BTN).click()

    def click_override_login_btn(self):
        # Checks if we have to force login or not
        elem = self.find_element(*self.locator.OVERRIDE_LOGIN_BTN)
        if elem:
            elem.click()
            print("Forcing login...")
            return
        print("Did not have to force login.")

    def click_all_counties_btn(self):
        self.find_element(*self.locator.ALL_COUNTIES_BTN).click()

    def enter_house_number(self):
        self.find_element(*self.locator.HOUSE_NUMBER_INPUT).send_keys(STREET_NUMBER)
    
    def enter_street_name(self):
        self.find_element(*self.locator.STREET_NAME_INPUT).send_keys(STREET_NAME)

    def click_search_btn(self):
        self.find_element(*self.locator.SEARCH_BTN).click()


    def login(self):
        self.enter_email()
        self.enter_password()
        self.click_login_btn()
        self.click_override_login_btn()

    def insert_property_address(self):
        self.enter_house_number()
        self.enter_street_name()
        self.click_search_btn()

    def run_full_test(self):
        print("Logging into geodata...")
        self.login()        
        print("Clicking all counties...")
        self.click_all_counties_btn()
        print("Inserting property address...")
        self.insert_property_address()
        
