from pages.base_page import BasePage
from utils.locators import TruePeopleLocators
from utils.env_loader import *
import time

class TruePeopleSearchPage(BasePage):
    def __init__(self, driver):
        self.locator = TruePeopleLocators
        super(TruePeopleSearchPage, self).__init__(driver, "https://www.truepeoplesearch.com/#")  # Python2 version
        self.new_tab()

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.REVERSE_ADDRESS_TAB) else False

    def click_reverse_address_tab(self):
        self.find_element(*self.locator.REVERSE_ADDRESS_TAB).click()

    def enter_street_number(self):
        self.find_element(*self.locator.STREET_ADDRESS_INPUT).send_keys(STREET_NUMBER + " ")
    
    def enter_street_name(self):
        self.find_element(*self.locator.STREET_ADDRESS_INPUT).send_keys(STREET_NAME + " ")

    def enter_city(self):
        self.find_element(*self.locator.CITY_STATE_ZIP_INPUT).send_keys(CITY + ", ")

    def enter_state(self):
        self.find_element(*self.locator.CITY_STATE_ZIP_INPUT).send_keys(STATE)

    def click_search_btn(self):
        self.find_element(*self.locator.SEARCH_BTN).click()

    def insert_property_address(self):
        self.enter_street_number()
        self.enter_street_name()
        self.enter_city()
        self.enter_state()

    def run_full_test(self):
        print("Clicking reverse propery address tab...")
        self.click_reverse_address_tab()
        print("Inserting property address...")
        self.insert_property_address()
        print("Clicking search...")
        self.click_search_btn()
