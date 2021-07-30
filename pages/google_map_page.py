from pages.base_page import BasePage
from utils.locators import GoogleMapLocators
from selenium.webdriver.support.ui import Select
from utils.env_loader import *
import time

class GoogleMapPage(BasePage):
    def __init__(self, driver):
        self.locator = GoogleMapLocators
        super(GoogleMapPage, self).__init__(driver, "https://www.google.com/maps/")  # Python2 version
        self.new_tab()

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.HOUSE_NUMBER_INPUT) else False

    def enter_street_number(self):
        self.find_element(*self.locator.SEARCH_BOX_INPUT).send_keys(STREET_NUMBER + " ")
    
    def enter_street_name(self):
        self.find_element(*self.locator.SEARCH_BOX_INPUT).send_keys(STREET_NAME + " ")

    def enter_street_suffix(self):
        self.find_element(*self.locator.SEARCH_BOX_INPUT).send_keys(SUFFIX + " ")  

    def enter_city(self):
        self.find_element(*self.locator.SEARCH_BOX_INPUT).send_keys(CITY + ", ")

    def enter_state(self):
        self.find_element(*self.locator.SEARCH_BOX_INPUT).send_keys(STATE)

    def click_search_btn(self):
        self.find_element(*self.locator.SEARCH_BTN).click()

    def insert_property_address(self):
        self.enter_street_number()
        self.enter_street_name()
        self.enter_street_suffix()
        self.enter_city()
        self.enter_state()

    def run_full_test(self):
        print("Inserting property address...")
        self.insert_property_address()
        print("Clicking go button...")
        self.click_search_btn()
        time.sleep(2)
