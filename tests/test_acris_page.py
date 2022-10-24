from tests.base_test import BaseTest
from pages.acris_page import *
from utils.addToCSV import add_property_to_csv

class TestAcrisPage(BaseTest):

    def test_inserting_property_address(self):
        print("Adding property to addresses.csv\n")
        add_property_to_csv()
        
        print("Starting with Acris.")
        page = AcrisPage(self.driver)
        page.run_full_test()
        print("Finished with Acris.")
