from pages.base_page import BasePage
from utils.locators import AcrisLocators
from utils.env_loader import *
import time

class AcrisPage(BasePage):
    def __init__(self, driver):
        self.locator = AcrisLocators
        super(AcrisPage, self).__init__(driver, "https://a836-acris.nyc.gov/CP/LookUp/Index")  # Python2 version
        self.new_tab()

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.COUNTY) else False

    def enter_county(self):
        self.find_element(*self.locator.COUNTY).send_keys(COUNTY)

    def enter_street_number(self):
        self.find_element(*self.locator.STREET_NUMBER).send_keys(STREET_NUMBER)
    
    def enter_street_name(self):
        self.find_element(*self.locator.STREET_NAME).send_keys(STREET_NAME + " ")

    def enter_unit_number(self):
        self.find_element(*self.locator.UNIT).send_keys(UNIT)

    def click_find_bbl(self):
        self.find_element(*self.locator.FIND_BBL).click()

    def click_doc_search(self):
        self.find_element(*self.locator.DOCUMENT_SEARCH).click()

    def click_search(self):
        self.find_element(*self.locator.SEARCH).click()

    def find_search_options(self):
        self.find_element(*self.locator.FINAL_SEARCH_OPTIONS)

    def insert_property_address(self):
        self.enter_county()
        self.enter_street_number()
        self.enter_street_name()
        self.enter_unit_number()

    def run_full_test(self):
        print("Inserting property address...")
        self.insert_property_address()
        print("Clicking find bbl button...")
        self.click_find_bbl()
        print("Clicking document search button...")
        self.click_doc_search()
        print("Clicking search button on second page...")
        self.click_search()
        print("Validing we reached end page...")
        self.find_search_options()

