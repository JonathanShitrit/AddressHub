from pages.base_page import BasePage
from utils.locators import NYCGovLocators
from selenium.webdriver.support.ui import Select
from utils.env_loader import *
import time

class NYCGovPage(BasePage):
    def __init__(self, driver):
        self.locator = NYCGovLocators
        url = "https://a810-bisweb.nyc.gov/bisweb/PropertyProfileOverviewServlet?boro={}&houseno={}&street={}&go2=+GO+&requestid=0".format(get_boro_id(), STREET_NUMBER, STREET_NAME)
        super().__init__(driver, url)
        self.new_tab()

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.HOUSE_NUMBER_INPUT) else False

    def enter_street_number(self):
        self.find_element(*self.locator.HOUSE_NUMBER_INPUT).send_keys(STREET_NUMBER)
    
    def enter_street_name(self):
        self.find_element(*self.locator.STREET_NAME_INPUT).send_keys(STREET_NAME + " ")

    def select_from_dropdown(self):
        Select(self.find_element(*self.locator.BORO_DROPDOWN)).select_by_value(get_boro_id())

    def click_go_btn(self):
        self.find_element(*self.locator.GO_BTN).click()

    def insert_property_address(self):
        self.enter_street_number()
        self.enter_street_name()
        self.select_from_dropdown()

    def run_full_test(self):
        print("Inserting property address...")
        self.insert_property_address()
        print("Clicking go button...")
        self.click_go_btn()

    def run_empty_test(self):
        pass