import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.google_sheet import GoogleSheet
from utils.env_loader import *

# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>
class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        # options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=1080,1080")
        options.add_experimental_option("detach", True)
        options.page_load_strategy = 'eager'
        # options.add_argument("--enable-automation")
        # options.add_argument("--start-fullscreen")
        # options.add_experimental_option("excludeSwitches", ['enable-automation'])
        sheet = GoogleSheet()
        property = [STREET_NUMBER, STREET_NAME, UNIT, CITY, COUNTY, STATE]
        sheet.add_address_to_sheet(property)

        print("Starting up!")

        global d
        chrome_path = ChromeDriverManager().install()
        if "THIRD_PARTY_NOTICES.chromedriver" in chrome_path:
            chrome_path = chrome_path.replace("THIRD_PARTY_NOTICES.chromedriver", "chromedriver")

        d = webdriver.Chrome(options=options)
        # d = webdriver.Chrome(options=options)
        self.driver = d
        

    # def tearDown(self):
    #     print(999)
    #     self.driver.close()